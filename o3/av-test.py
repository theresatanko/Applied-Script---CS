# This is a simple AV/EDR test script written for the Applied Script course.



#!/usr/bin/env python3
import os
import time
import platform
import sys

# Check operating system
system = platform.system()
print(f"Operating system: {system}")

# Only allow the rest of the script to run on Windows, stop on all other systems
if system == "Windows":
    print("Windows detected. The script will continue...")
elif system == "Linux":
   print("Linux detected. This script is intended for Windows.")
   sys.exit(1)
elif system == "Darwin":
   print("macOS detected. This script is intended for Windows.")
   sys.exit(1)
else:
    print(f"Unknown operating system ({system}). This script is intended for Windows. Stopping execution.")
    sys.exit(1)

# EICAR antivirus test string (harmless). The string is harmless but must match exactly for the antivirus to react
eicar_str = "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"


# Create test file in the user's home directory. This keeps the file in a location where the user normally has write access
filename = "eicar_test.txt"
filepath = os.path.join(os.path.expanduser("~"), filename)
print(f"Creating test file: {filepath}")

# Write test file. If something goes wrong, print the error and stop the script
try:
    with open(filepath, "w") as f:
        f.write(eicar_str)
    print("EICAR test file created.")
except Exception as e:
    print("Could not create the file.")
    print(e)
    sys.exit(1)

# Delay – wait for AV/EDR response. Pause for a short time to give the AV/EDR engine a chance to scan the new file
print("Waiting 3 seconds for possible AV reaction...")
time.sleep(3)

# Check if the file exists and read it. This helps us see if the AV/EDR solution has removed or changed the file
try:
    with open(filepath, "r", encoding="ascii") as f:
        file_content = f.read()

    if file_content == eicar_str:
        print("The file is still present and the content matches the EICAR signature.")
        print("Antivirus did NOT block the file.")
    else:
        print("The file is present, but the content has changed.")
        print("Antivirus may have modified the file.")
except Exception as e:
    # If the file cannot be read at all, it is likely removed or quarantined by AV/EDR
    print("The file could not be read.")
    print("AV/EDR has probably removed or quarantined the file.")
    print("Your AV/EDR solution is working as expected.")

 