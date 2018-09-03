# -*- coding: utf-8 -*-


import os
import errno
import requests
import json
import click

from pkg_resources import Requirement


_GENERIC_ADDRESS = "https://pypi.org/pypi/{package}/json"


def build_package_cache(settings, package):
    """Download all package versions from PyPI for specified package."""

    pkg_urls = resolve_url_list(settings, package)
    total_entries = len(pkg_urls)

    if (total_entries == 0):
        return None
    else:
        with click.progressbar(length=total_entries, width=0, label='') as bar:
            for (project_name, file_name, url) in pkg_urls:
                bar.label = "{:32s}".format(file_name)
                target_folder = get_cache_subfolder(settings, project_name)
                target_file = os.path.join(target_folder, file_name)
                download_package(url, target_file)

                bar.update(1) # advance status bar
        return None


def resolve_url_list(settings, package):
    """Build a url list for packages matching the specifications."""

    requires = Requirement(package)

    package_addr = _GENERIC_ADDRESS.format(package=requires.name)
    package_data = requests.get(package_addr).json()
    
    all_versions = package_data["releases"].keys()
    wanted_versions = [v for v in all_versions if (requires.__contains__(v))]

    url_list = []
    accepted_types = settings['packagetypes']
    for version in wanted_versions:
        packages_for_version = package_data['releases'].get(version)
        for package in packages_for_version: 
            package_type = package['packagetype']
            file_name = str(package.get('filename'))  # file name
            url = str(package.get('url'))             # url
            project_name = str(requires.name)         # sub-folder in cache
            if (package_type in accepted_types):
                url_list.append((project_name, file_name, url))

    return url_list


def download_package(url, target_file):
    """Download contents at url-address to file."""

    if (not os.path.exists(target_file)):
        package_data = requests.get(url, allow_redirects=True)
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


def create_directory(dir_name):
    """Check if a directory exists and create it if it doesn't."""

    try:
        os.makedirs(dir_name)
    except OSError as e: 
        if e.errno != errno.EEXIST:
            raise
    
    return None

