"""Systemathics Ganymede APIs Token Helpers

This module helps to create channels to access Systemathics Ganymede authenticated APIs.

functions:
    * get_grpc_channel - Get a channel suitable to call Ganymede gRPC APIs.
    * get_aio_grpc_channel - Get an aio channel suitable to call Ganymede gRPC APIs.
"""

import os
from shutil import ExecError
import grpc

DEFAULT_ENDPOINT = "https://grpc.ganymede.cloud"

def get_grpc_channel() -> grpc.Channel:
    """
    Get a channel suitable to call Ganymede gRPC APIs.
    This uses the GRPC_APIS environment variable in the form http[s]://fdqn[:port] (if no scheme is give, we'll assume https).
    If none is detected, use DEFAULT_ENDPOINT.
    Note:
        For secure channels, we'll try to guess the path of CA certificates chain automatically.
        For windows you need to 'pip install wheel python-certifi-win32' for that to work (it exports Windows CA Store to a PEM file).
        In the event CA certificates cannot be found, or if you want to use a custom file, set the SSL_CERT_FILE environment variable.
    Returns:
        An aio channel suitable to call Ganymede gRPC APIs.
    """
    endpoint = os.getenv('GRPC_APIS','')
    endpoint = endpoint if endpoint else DEFAULT_ENDPOINT # if no endpoint was provided, use the default one
    endpoint = endpoint if endpoint.startswith("http") else f"https://{endpoint}" # if no scheme was provided, assume it's https
    if (endpoint.startswith("https")):
        return grpc.secure_channel(endpoint.replace("https://",""), _get_channel_credentials())
    else:
        return grpc.insecure_channel(endpoint.replace("http://",""))

def get_aio_grpc_channel() -> grpc.aio.Channel:
    """
    Get an aio channel suitable to call Ganymede gRPC APIs.
    This uses the GRPC_APIS environment variable in the form http[s]://fdqn[:port].
    If none is detected, use DEFAULT_ENDPOINT.
    Note:
        For secure channels, we'll try to guess the path of CA certificates chain automatically.
        For windows you need to 'pip install wheel python-certifi-win32' for that to work (it exports Windows CA Store to a PEM file).
        In the event CA certificates cannot be found, or if you want to use a custom file, set the SSL_CERT_FILE environment variable.
    Returns:
        An aio channel suitable to call Ganymede gRPC APIs.
    """
    endpoint = os.getenv('GRPC_APIS','')
    endpoint = endpoint if endpoint else DEFAULT_ENDPOINT # if no endpoint was provided, use the default one
    endpoint = endpoint if endpoint.startswith("http") else f"https://{endpoint}" # if no scheme was provided, assume it's https
    if (endpoint.startswith("https")):
        return grpc.aio.secure_channel(endpoint.replace("https://",""), _get_channel_credentials())
    else:
        return grpc.aio.insecure_channel(endpoint.replace("http://",""))

def _get_channel_credentials() -> grpc.ChannelCredentials:
    # If we have a SSL_CERT_FILE env variable, use it
    ssl_cert_file = os.getenv('SSL_CERT_FILE','')
    if (ssl_cert_file !='' ):
        if (not(os.path.isfile(ssl_cert_file))):
            print(f"warn: Found SSL_CERT_FILE={ssl_cert_file} environment variable, but file doesn't exist!")
        cabundle = ssl_cert_file
    # Otherwise try autodetection
    else:
        cabundle = _autodetect_ca_bundle()

    with open(cabundle, 'rb') as f:
        credentials = grpc.ssl_channel_credentials(f.read())
        return credentials

def _autodetect_ca_bundle() -> str:
    cabundles = [
	"/etc/ssl/certs/ca-certificates.crt",                                  # Debian/Ubuntu/Gentoo/etc..
	"/etc/pki/tls/certs/ca-bundle.crt",                                    # Fedora/RHEL 6
	"/etc/ssl/ca-bundle.pem",                                              # OpenSUSE
	"/etc/pki/tls/cacert.pem",                                             # OpenELEC
	"/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem",                   # CentOS/RHEL 7
	"/etc/ssl/cert.pem",                                                   # Alpine Linux
    os.path.join(os.getenv('LOCALAPPDATA',''), '.certifi', 'cacert.pem')   # Windows (requires: pip install wheel python-certifi-win32)
    ]

    for cabundle in cabundles:
        if (os.path.isfile(cabundle)):
            return cabundle

    raise Exception(f"Could not auto detect trusted root certificates file, tried {cabundles}. Please help by setting SSL_CERT_FILE environment variable")
