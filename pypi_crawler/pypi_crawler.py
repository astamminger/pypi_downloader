#!/usr/bin/env python

import requests

_GENERIC_ADDRESS = "https://pypi.org/pypi/{package}/json"

def build_package_cache(settings, package_list):
    """Download all package version for specified package list"""

    for package in package_list:
        package_pypi_address = _GENERIC_ADDRESS.format(package=package)
        package_info = requests.get(package_pypi_address).json()

        print(package_info)
        
