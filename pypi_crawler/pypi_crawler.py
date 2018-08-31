#!/usr/bin/env python

import requests

_GENERIC_ADDRESS = "https://pypi.org/pypi/{package}/json"

def create_directory(dirname):
    """Check if a directory exists and create it if it doesn't."""

    try:
        os.makedirs(dirname)
    except OSError as e: 
        if e.errno != errno.EEXIST:
            raise
    
    return None

def build_package_cache(settings, package):
    """Download all package versions from PyPI for specified package."""

    for package in package_list:
        package_pypi_address = _GENERIC_ADDRESS.format(package=package)
        package_info = requests.get(package_pypi_address).json()

        print(package_info)

