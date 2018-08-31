#!/usr/bin/env python


import os
import errno
import requests
import json

from pkg_resources import Requirement


_GENERIC_ADDRESS = "https://pypi.org/pypi/{package}/json"


def build_package_cache(settings, package):
    """Download all package versions from PyPI for specified package."""

    



def resolve_url_list(package):
    """Build a url list for packages matching the specifications."""

    requires = Requirement(package)

    package_addr = _GENERIC_ADDRESS.format(package=requires.name)
    package_data = requests.get(package_addr).json()
    
    all_versions = package_data["releases"].keys()
    wanted_versions = [v for v in all_versions if (requires.__contains__(v))]

    url_list = []
    for version in wanted_versions:
        package_info = package_data['releases'].get(version)
        filename = str(package_info.get('filename')) # file name
        url = str(package_info.get('url'))           # url
        project_name = str(filename.split('-')[0])   # sub-folder in cache
        url_list.append((project_name, filename, url))

    return url_list


def download_package(url, target_file):
    """Download contents at url-address to file."""

    if (not os.path.exists(target_file)):
        package_data = request.get(url, allow_redirects=True)
        with open(target_file, 'wb') as target:
            target.write(package_data.content)
    else: # skip if file is already present in cache
        pass

    return None


def get_cache_subfolder(settings, project_name):
    """Checks and returns the subfolder for the defined project_name."""

    cache_folder = settings.get('cache_folder')
    target_folder = os.path.abspath(os.path.join(cache_folder, project_name))
    if (not os.path.exists(target_folder)):
        create_directory(target_folder)
    
    return target_folder


def create_directory(dirname):
    """Check if a directory exists and create it if it doesn't."""

    try:
        os.makedirs(dirname)
    except OSError as e: 
        if e.errno != errno.EEXIST:
            raise
    
    return None

