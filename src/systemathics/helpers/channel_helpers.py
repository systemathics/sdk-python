"""Systemathics APIs Token Helpers

This module helps to create tokens to access Systemathics authenticated APIs

functions:
    * get_channel_credentials - get a vanilla ChannelCredentials with default trusted root certificates (from SSL_CERT_FILE environment variable if set, or using auto dection if not)
    * autodetect_ca_bundle - automatically detect system wide trusted root certificates to use by probing well known OS paths.
    * get_grpc_api_endpoint - get the endpoint to connect to Systemathics APIs (from GRPC_APIS environment variable)
    * get_grpc_channel - get a gRPC channel to connect to Systemathics APIs with default credentials.
"""

import os
from shutil import ExecError
import grpc

def get_channel_credentials() -> grpc.ChannelCredentials:
    # If we have a SSL_CERT_FILE env variable, use it
    ssl_cert_file = os.getenv('SSL_CERT_FILE','')
    if (ssl_cert_file !='' ):
        if (not(os.path.isfile(ssl_cert_file))):
            print(f"warn: Found SSL_CERT_FILE={ssl_cert_file} environment variable, but file doesn't exist!")
        cabundle = ssl_cert_file
    # Otherwise try autodetection
    else:
        cabundle = autodetect_ca_bundle()

    with open(cabundle, 'rb') as f:
        credentials = grpc.ssl_channel_credentials(f.read())
        return credentials

def autodetect_ca_bundle() -> str:
    cabundles = [
	"/etc/ssl/certs/ca-certificates.crt",                # Debian/Ubuntu/Gentoo/etc..
	"/etc/pki/tls/certs/ca-bundle.crt",                  # Fedora/RHEL 6
	"/etc/ssl/ca-bundle.pem",                            # OpenSUSE
	"/etc/pki/tls/cacert.pem",                           # OpenELEC
	"/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem", # CentOS/RHEL 7
	"/etc/ssl/cert.pem"                                  # Alpine Linux
                                                         # Windows ?
    ]

    for cabundle in cabundles:
        if (os.path.isfile(cabundle)):
            return cabundle

    raise Exception(f"Could not find any trusted root certificates file, tried {cabundles}")

def get_grpc_api_endpoint() -> str:
    grpc_apis = os.getenv('GRPC_APIS','')
    if (grpc_apis == ''):
        raise Exception("Environment variable GRPC_APIS is not set!")
    return grpc_apis

def get_grpc_channel() -> grpc.Channel:
    credentials = get_channel_credentials()
    return grpc.secure_channel(get_grpc_api_endpoint(), credentials)