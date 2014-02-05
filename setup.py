"""
Installer for the ADS C modules.
"""

import os
import sys
from distutils.core import setup
from distutils.extension import Extension

MODULES = ['Looker', 'ctrigram', 'ldw']

EXTENSIONS = [Extension(name=mod, sources=[mod + 'module.c'])
        for mod in MODULES]

setup (
     name         = "ads_modules",
     version      = "2.0",
     description  = "Looker and other modules for ADS system",
     author       = "Markus Demleitmer",
     author_email = "mdemleit@tucana.harvard.edu",
     url          = "http://adsabs.harvard.edu",
     ext_modules  = EXTENSIONS,
)
