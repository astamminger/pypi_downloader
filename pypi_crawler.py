#!/usr/bin/env python

import configparser
import requests

generic_address = "https://pypi.org/pypi/{package}/json"

package = "aiida"

request = requests.get(generic_address.format(package=package)).json()

