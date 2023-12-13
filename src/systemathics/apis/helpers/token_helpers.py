"""Systemathics Ganymede  API Token Helpers

This module helps to create tokens to access Systemathics Ganymede authenticated API.

functions:
    * get_token - Get a JWT Authorization token suitable to call Ganymede gRPC API.
"""

import os
import http.client
import json
import pathlib
import urllib.request
import jwt
import logging

DEFAULT_AUDIENCE = "https://ganymede-prod"

DEFAULT_TENANT = "ganymede-prod.eu.auth0.com"

def get_token_as_metadata() -> []:
    """
    Get a JWT Authorization token suitable to call Ganymede gRPC API.
    We either use 'AUTH0_TOKEN' environment variable (if present) to create a bearer token from it.
    Or 'CLIENT_ID' and 'CLIENT_SECRET' environment variables (optionally 'AUDIENCE' can override DEFAULT_AUDIENCE, and 'TENANT' can override DEFAULT_TENANT).  
    Returns:
        A JWT Authorization token suitable to call Ganymede gRPC API in a form directly assignable to metadata= in stub call, that is [('authorization', get_token())].
    """
    return [('authorization', get_token())]

def get_token() -> str:    
    """
    Get a JWT Authorization token suitable to call Ganymede gRPC API.
    We either use 'AUTH0_TOKEN' environment variable (if present) to create a bearer token from it.
    Or 'CLIENT_ID' and 'CLIENT_SECRET' environment variables (optionally 'AUDIENCE' can override DEFAULT_AUDIENCE, and 'TENANT' can override DEFAULT_TENANT).  
    Returns:
        A JWT Authorization token suitable to call Ganymede gRPC API.
    """
    auth0_token = os.getenv("AUTH0_TOKEN","")
    client_id = os.getenv("CLIENT_ID","")
    client_secret = os.getenv("CLIENT_SECRET","")
    audience = os.getenv("AUDIENCE","")
    audience = audience if audience else DEFAULT_AUDIENCE
    tenant = os.getenv("TENANT","")
    tenant = tenant if tenant else DEFAULT_TENANT
    
    # If we have a token in AUTH0_TOKEN env var, use it as is
    if (auth0_token):
        logging.debug(f"get_token: Using token from AUTH0_TOKEN")
        return f"Bearer {auth0_token}" # valid, use it

    # If we have a persisted token
    tokendir = os.path.join(str(pathlib.Path.home()), ".systemathics")
    tokenfile = os.path.join(tokendir, _cleanup(tenant) + "_" + _cleanup(audience) + ".auth0_token.txt")
    if os.path.exists(tokenfile):
        with open(tokenfile, 'r') as input:
            auth0_token = input.read()

    if (auth0_token):
        if (_validate_token(auth0_token, tenant, audience, "from file " + tokenfile)):
            logging.debug(f"get_token: Using token from {tokenfile}")
            return f"Bearer {auth0_token}" # valid, use it
        else:
            logging.debug(f"get_token: Deleting {tokenfile} (invalid)")
            os.remove(tokenfile) # invalid, delete it
            
    # At this stage, if we don't have a valid token, ask one using Auth0 REST API (we need CLIENT_ID and CLIENT_SECRET; Optionally AUDIENCE and TENANT)
    if (client_id and client_secret):
        return _request_token_using_auth0_rest_api(
            client_id, 
            client_secret, 
            audience, 
            tenant)
    else:    
        raise Exception(f"You need to set CLIENT_ID and CLIENT_SECRET (and optionally AUDIENCE and TENANT) environment variables in order to be able to request tokens")

def _request_token_using_auth0_rest_api(client_id, client_secret, audience, tenant) -> str:
    if (client_id == ""):
        raise Exception(f"client_id cannot be null")
    if (client_secret == ""):
        raise Exception(f"client_secret cannot be null")
    if (audience == ""):
        raise Exception(f"audience cannot be null")
    if (tenant == ""):
        raise Exception(f"tenant cannot be null")

    logging.debug(f"_request_token_using_auth0_rest_api: Calling auth0 API at {tenant} to get a token")

    # Setup connection and payload
    conn = http.client.HTTPSConnection(tenant)
    headers = { "content-type": "application/json" }
    params = {"client_id": client_id, "client_secret": client_secret, "grant_type" : "client_credentials", "audience": audience }
    payload = json.dumps(params)

    # Send Request
    conn.request("POST", "/oauth/token", payload, headers)
    res = conn.getresponse()
    data = res.read()
       
    json_data =  json.loads(data.decode("utf-8"))
                            
    # Get access token to be used to authenticate against API
    try:
        token = f"{json_data['token_type']} {json_data['access_token']}"
    except Exception:
        raise Exception(f"Returned JSON doesn't contain 'token_type' and/or 'access_token'. Check your client ID, client secret, audience and tenant: {json_data}")
    
    if not _validate_token(json_data['access_token'], tenant, audience, "from AUTH0 REST API"):       
        raise Exception(f"Token returned by Auth0 API is invalid !")
            
    # Push to environment
    os.environ['AUTH0_TOKEN'] = json_data['access_token']
    logging.debug(f"_request_token_using_auth0_rest_api: Pushed token to env AUTH0_TOKEN")
        
    # Push to file
    tokendir = os.path.join(str(pathlib.Path.home()), ".systemathics")
    tokenfile = os.path.join(tokendir, _cleanup(tenant) + "_" + _cleanup(audience) + ".auth0_token.txt")
    if not os.path.exists(tokendir):
        os.makedirs(tokendir)
    if os.path.exists(tokenfile):
        os.remove(tokenfile)
    with open(tokenfile, 'w') as output:
        output.write(json_data['access_token'])
        logging.debug(f"_request_token_using_auth0_rest_api: Pushed token to file {tokenfile}")
    return token

def _cleanup(input: str) -> str:
    str2 = input
    str2 = str2.replace('https://','')
    str2 = str2.replace('http://','')
    str2 = str2.replace('/','')
    str2 = str2.replace('\\','')
    str2 = str2.replace(':','')
    return str2
    
def _validate_token(token: str, tenant: str, audience: str, token_label: str) -> bool:
    # public key local dir/path
    pubkeydir = os.path.join(str(pathlib.Path.home()), ".systemathics")
    pubkeyfile = os.path.join(pubkeydir, _cleanup(tenant) + ".jwks.json")
    if not os.path.exists(pubkeydir):
        os.makedirs(pubkeydir)
    
    # cache
    if not os.path.exists(pubkeyfile):
        try:
            url = f'https://{tenant}/.well-known/jwks.json'
            logging.debug(f"_validate_token: Downloading public key at {url} to {pubkeyfile}")
            with urllib.request.urlopen(url) as input:
                with open(pubkeyfile, 'wb') as output:
                    pubkey = input.read()
                    output.write(pubkey)
        except urllib.error.URLError as e:
            logging.error(f"Could not get {url}: {e.reason}")
            raise
    
    jwks_url = "file:///" + pubkeyfile    
    logging.debug(f"_validate_token: Using public key store at {jwks_url}")
    jwks_client = jwt.PyJWKClient(jwks_url)
    header = jwt.get_unverified_header(token)
    kid = header["kid"]
    alg = [header["alg"]]
    key = jwks_client.get_signing_key(kid).key
    try:
        logging.debug(f"_validate_token: Validating token {token_label} with kid={kid} alg={alg} tenant={tenant} audience={audience}")
        jwt.decode(token, key, alg, audience=audience)
        logging.debug(f"_validate_token: Validated token {token_label} with kid={kid} alg={alg} tenant={tenant} audience={audience}")
        return True
    except jwt.exceptions.ExpiredSignatureError as expiredError:
        logging.error(f"_validate_token: Token is expired: {expiredError}")
        return False 
    except jwt.exceptions.DecodeError as decodeError:
        logging.error(f"_validate_token: Token could not be decoded: {decodeError}")
        return False 
    except Exception as ex:
        logging.error(f"_validate_token: Token is invalid: {ex}")
        return False   
