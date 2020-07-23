# SECUREAUTH LABS. Copyright 2019 SecureAuth Corporation. All rights reserved.
#
# This software is provided under under a slightly modified version
# of the Apache Software License. See the accompanying LICENSE file
# for more information.
#
import pkg_resources
from impacket import __path__

BANNER = "Impacket - Exchanger.py Fork\n"

def getInstallationPath():
    return 'Impacket Library Installation Path: {}'.format(__path__[0])
