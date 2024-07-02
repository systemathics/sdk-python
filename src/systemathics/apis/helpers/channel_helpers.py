"""Systemathics Ganymede API Token Helpers

This module helps to create channels to access Systemathics Ganymede authenticated API.

functions:
    * get_grpc_channel - Get a channel suitable to call Ganymede gRPC API.
    * get_aio_grpc_channel - Get an aio channel suitable to call Ganymede gRPC API.
"""

import os
import grpc
import urllib.request
import pathlib
    
DEFAULT_ENDPOINT = "https://grpc.ganymede.cloud"

def get_grpc_channel(endpoint : str = "", **kwargs) -> grpc.Channel:
    """
    Get a channel suitable to call Ganymede gRPC API.
    If no endpoint parameter is given, try to use GRPC_APIS environment variable or fallback to DEFAULT_ENDPOINT.
    Note:
        For secure channels, we'll try to guess the path of CA certificates chain automatically, or download one from Mozilla official site.
        In the event CA certificates cannot be found, or if you want to use a custom file, set the SSL_CERT_FILE environment variable.
    Returns:
        A channel suitable to call Ganymede gRPC API.
    """
    endpoint = endpoint if endpoint else os.getenv('GRPC_APIS','')
    endpoint = endpoint if endpoint else DEFAULT_ENDPOINT # if no endpoint was provided, use the default one
    endpoint = endpoint if endpoint.startswith("http") else f"https://{endpoint}" # if no scheme was provided, assume it's https
    return _get_grpc_channel(endpoint, **kwargs)
    
def _get_grpc_channel(endpoint: str, **kwargs) -> grpc.Channel:
    if not endpoint or not endpoint.startswith("http"):
        raise "endpoint should have scheme http or https"
    options = [ (arg,kwargs[arg]) for arg in kwargs ]
    if (endpoint.startswith("https")):
        return grpc.secure_channel(endpoint.replace("https://",""), _get_channel_credentials(),  options = options)
    else:
        return grpc.insecure_channel(endpoint.replace("http://",""), options = options)

def get_aio_grpc_channel(endpoint = "", **kwargs) -> grpc.aio.Channel:
    """
    Get an aio channel suitable to call Ganymede gRPC API.
    If no endpoint parameter is given, try to use GRPC_APIS environment variable or fallback to DEFAULT_ENDPOINT.
    Note:
        For secure channels, we'll try to guess the path of CA certificates chain automatically, or download one from Mozilla official site.
        In the event CA certificates cannot be found, or if you want to use a custom file, set the SSL_CERT_FILE environment variable.
    Returns:
        An aio channel suitable to call Ganymede gRPC API.
    """
    endpoint = endpoint if endpoint else os.getenv('GRPC_APIS','')
    endpoint = endpoint if endpoint else DEFAULT_ENDPOINT # if no endpoint was provided, use the default one
    endpoint = endpoint if endpoint.startswith("http") else f"https://{endpoint}" # if no scheme was provided, assume it's https
    return _get_aio_grpc_channel(endpoint, **kwargs)

def _get_aio_grpc_channel(endpoint: str, **kwargs) -> grpc.aio.Channel:
    if not endpoint or not endpoint.startswith("http"):
        raise "endpoint should have scheme http or https"
    options = [ (arg,kwargs[arg]) for arg in kwargs ]
    if (endpoint.startswith("https")):
        return grpc.aio.secure_channel(endpoint.replace("https://",""), _get_channel_credentials(), options = options )
    else:
        return grpc.aio.insecure_channel(endpoint.replace("http://",""), options = options )

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

def _get_current_mozilla_cacert() -> str:
    # up to date CA bundle (the official one embedded in Mozilla)
    url = "http://curl.haxx.se/ca/cacert.pem"
    
    # local path for CA bundle
    cadir = os.path.join(str(pathlib.Path.home()), ".systemathics")
    cafile = os.path.join(cadir, "cacert.pem")
    if not os.path.exists(cadir):
        os.makedirs(cadir)
    
    # don't redownload
    if os.path.exists(cafile):
        return cafile
    
    try:
        with urllib.request.urlopen(url) as input:
            with open(cafile, 'wb') as output:
                output.write(input.read())
    except urllib.error.URLError as e:
        print(f"Could not get {url}: {e.reason}")
           
    return cafile

def _autodetect_ca_bundle() -> str:
    cabundles = [
	"/etc/ssl/certs/ca-certificates.crt",                                  # Debian/Ubuntu/Gentoo/etc..
	"/etc/pki/tls/certs/ca-bundle.crt",                                    # Fedora/RHEL 6
	"/etc/ssl/ca-bundle.pem",                                              # OpenSUSE
	"/etc/pki/tls/cacert.pem",                                             # OpenELEC
	"/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem",                   # CentOS/RHEL 7
	"/etc/ssl/cert.pem",                                                   # Alpine Linux
    os.path.join(os.getenv('LOCALAPPDATA',''), '.certifi', 'cacert.pem')   # Windows (for those who installed python-certifi-win32, now defunct, e.i: pip install wheel python-certifi-win32)
    ]

    # probe
    for cabundle in cabundles:
        if (os.path.isfile(cabundle)):
            print(f"Using CA bundle {cabundle}")
            return cabundle

    # fallback to current mozilla trusted root CA certificate chain
    cabundle = _get_current_mozilla_cacert()
    print(f"Using CA bundle {cabundle}")
    return cabundle
