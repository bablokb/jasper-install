# -----------------------------------------------------------------------------
# Jasper-module to reboot the computer.
#
# This has nothing to do with the main purpose of this project, but
# I just want to provide this module as is.
#
# This file is part of the project http://github.com/bablokb/jasper-install
#
# Copyright Bernhard Bablok (mail at bablokb dot de)
#
# Released under the GPL V3
#
# -----------------------------------------------------------------------------

import re
import os

WORDS = ["REBOOT", "YES", "OKAY", "NO"]

def isValid(text):
    return bool(re.search(r'\breboot\b', text, re.IGNORECASE))

def handle(text, mic, profile):
  mic.say("Really reboot the system now?")
  response = mic.activeListen()
  if bool(re.search(r'\b(yes|okay)\b',response,re.IGNORECASE)):
    mic.say("Initiating reboot. Please wait for system restart")
    os.system("sudo reboot")
  else:
    mic.say("Reboot cancelled")


