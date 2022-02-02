"""Systemathics Ganymede  APIs Token Helpers

This module helps to create tokens to access Systemathics Ganymede authenticated APIs.

functions:
    * get_token - Get a JWT Authorization token suitable to call Ganymede gRPC APIs.
"""

import os
import http.client
import json

DEFAULT_AUDIENCE = "https://prod.ganymede-prod"

DEFAULT_TENANT = "ganymede-prod.eu.auth0.com"

def get_token_as_metadata() -> []:
    """
    Get a JWT Authorization token suitable to call Ganymede gRPC APIs.
    We either use 'AUTH0_TOKEN' environment variable (if present) to create a bearer token from it.
    Or 'CLIENT_ID' and 'CLIENT_SECRET' environment variables (optionally 'AUDIENCE' can override DEFAULT_AUDIENCE, and 'TENANT' can override DEFAULT_TENANT).  
    Returns:
        A JWT Authorization token suitable to call Ganymede gRPC APIs in a form directly assignable to metadata= in stub call, that is [('authorization', get_token())].
    """
    return [('authorization', get_token())]

def get_token() -> str:    
    """
    Get a JWT Authorization token suitable to call Ganymede gRPC APIs.
    We either use 'AUTH0_TOKEN' environment variable (if present) to create a bearer token from it.
    Or 'CLIENT_ID' and 'CLIENT_SECRET' environment variables (optionally 'AUDIENCE' can override DEFAULT_AUDIENCE, and 'TENANT' can override DEFAULT_TENANT).  
    Returns:
        A JWT Authorization token suitable to call Ganymede gRPC APIs.
    """
    auth0_token = os.getenv("AUTH0_TOKEN","")
    client_id = os.getenv("CLIENT_ID","")
    client_secret = os.getenv("CLIENT_SECRET","")
    audience = os.getenv("AUDIENCE","")
    tenant = os.getenv("TENANT","")

    # If we have AUTH0_TOKEN, generate a bearer token
    if(auth0_token != ""):
        return f"Bearer {auth0_token}"

    # If we don't, use Auth0 REST API to request one (we need CLIENT_ID and CLIENT_SECRET; Optionally AUDIENCE and TENANT)
    if (client_id and client_secret):
        return _create_bearer_token_using_rest(
            client_id, 
            client_secret, 
            audience if audience else DEFAULT_AUDIENCE, 
            tenant if tenant else DEFAULT_TENANT)
    else:    
        raise Exception(f"AUTH0_TOKEN environment variable is not set, therefore CLIENT_ID and CLIENT_SECRET (and optionally AUDIENCE and TENANT) environment variables must be set")

def _create_bearer_token_using_rest(client_id, client_secret, audience, tenant) -> str:
    if (client_id == ""):
        raise Exception(f"client_id cannot be null")
    if (client_secret == ""):
        raise Exception(f"client_secret cannot be null")
    if (audience == ""):
        raise Exception(f"audience cannot be null")
    if (tenant == ""):
        raise Exception(f"tenant cannot be null")

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
        os.environ['AUTH0_TOKEN'] = json_data['access_token'] # Push to environment
        return token
    except Exception as ee:
        raise Exception(f"Returned JSON doesn't contain 'token_type' and/or 'access_token'. Check your client ID, client secret, audience and tenant: {json_data}")
