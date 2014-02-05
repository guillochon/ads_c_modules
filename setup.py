"""
Installer for the ADS C modules.
"""

import os
import sys
from distutils.core import setup
from distutils.extension import Extension
from ads.ads_c_modules.utils import get_platform_specific_module

MODULES = ['Looker', 'ctrigram', 'ldw']

PLATFORM_DIR = 'ads_c_modules/' + get_platform_specific_module()

print sys.argv

if len(sys.argv) > 1 and sys.argv[1] == 'install':
    print "Installing in " + PLATFORM_DIR
    if not os.path.exists('../' + PLATFORM_DIR):
        os.makedirs('../' + PLATFORM_DIR)
        os.system('touch ../' + PLATFORM_DIR + '/__init__.py')

EXTENSIONS = [Extension(name=mod, sources=[mod + 'module.c'])
        for mod in MODULES]

setup (
     name         = "ads_modules",
     version      = "2.0",
     description  = "Looker and other modules for ADS system",
     author       = "Markus Demleitmer",
     author_email = "mdemleit@tucana.harvard.edu",
     url          = "http://adsabs.harvard.edu",
     extra_path   = 'ads/' + PLATFORM_DIR,
     ext_modules  = EXTENSIONS,
)
