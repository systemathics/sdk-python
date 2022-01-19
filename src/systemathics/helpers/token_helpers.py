"""Systemathics APIs Token Helpers

This module helps to create tokens to access Systemathics authenticated APIs

functions:
    * get_token - get token by autodecting environment variables
    * create_bearer_token - create a bearer token (used by get_token when AUTH0_TOKEN env variable is set)
    * create_oauth_token - create oauth token (used by get_token when AUTH0_TOKEN env variable is not set and CLIENT_ID, CLIENT_SECRET, AUDIENCE and TENANT environment variables are set)
"""

import os
import http.client
import json

def get_token() -> str:    
    auth0_token = os.getenv('AUTH0_TOKEN','')
    client_id = os.getenv('CLIENT_ID','')
    client_secret = os.getenv('CLIENT_SECRET','')
    audience = os.getenv('AUDIENCE','')
    tenant = os.getenv('TENANT','')

    # If we have AUTH0_TOKEN, generate a bearer token
    if(auth0_token != ''):
        if (client_id != ''):
            print(f"print: AUTH0_TOKEN environment variable is set, CLIENT_ID environment variable will be ignored")
        if (client_secret != ''):
            print(f"print: AUTH0_TOKEN environment variable is set, CLIENT_SECRET environment variable will be ignored")
        if (audience != ''):
            print(f"print: AUTH0_TOKEN environment variable is set, AUDIENCE environment variable will be ignored")
        if (tenant != ''):
            print(f"print: AUTH0_TOKEN environment variable is set, TENANT environment variable will be ignored")
        return create_bearer_token(auth0_token)

    # If we don't, look for CLIENT_ID, CLIENT_SECRET, AUDIENCE and TENANT to create a token using Auth0 API
    missing=[]
    if(client_id == ''):
        missing.append("CLIENT_ID")
    if(client_secret == ''):
        missing.append("CLIENT_SECRET")
    if(audience == ''):
        missing.append("AUDIENCE")
    if(tenant == ''):
        missing.append("TENANT")

    if (len(missing) == 0):
        return create_oauth_token(client_id, client_secret, audience, tenant)
        
    raise Exception(f"AUTH0_TOKEN environment variable is not set, therefore CLIENT_ID, CLIENT_SECRET, AUDIENCE and TENANT environment variables must be set. Missing env variables {missing}")

def create_bearer_token(auth0_token) -> str:
    if (auth0_token == ''):
        raise Exception(f"auth0_token cannot be null")

    return f"Bearer {auth0_token}"

def create_oauth_token(client_id, client_secret, audience, tenant) -> str:
    if (client_id == ''):
        raise Exception(f"client_id cannot be null")
    if (client_secret == ''):
        raise Exception(f"client_secret cannot be null")
    if (audience == ''):
        raise Exception(f"audience cannot be null")
    if (tenant == ''):
        raise Exception(f"tenant cannot be null")

    # Setup connection and payload
    conn = http.client.HTTPSConnection(tenant)
    headers = { 'content-type': "application/json" }
    params = {"client_id": client_id, "client_secret": client_secret, "grant_type" : "client_credentials", "audience": audience }
    payload = json.dumps(params)

    # Send Request
    conn.request("POST", "/oauth/token", payload, headers)
    res = conn.getresponse()
    data = res.read()
    json_data =  json.loads(data.decode("utf-8"))
                        
    # Get access token to be used to authenticate against API
    token = f"{json_data['token_type']} {json_data['access_token']}"

    return token
