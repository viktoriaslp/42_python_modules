#!/usr/bin/env python3

import os
import site
import sys

# If both prefixes are the same, Python is running in the global environment
if sys.prefix == sys.base_prefix:
    print("MATRIX STATUS: You're still plugged in\n")

    # Path to the Python interpreter that is currently running this script
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n") 
    print("WARNING: You're in the global environment!") 
    print("The machines can see everything you install.\n")

    print(
        "To enter the construct, run:",
        "python -m venv matrix_env",
        "source matrix_env/bin/activate # On Unix",
        "matrix_env",
        "Scripts",
        "activate",
        "# On Windows",
        sep="\n"
    )

    print("\nThen run this program again.")
else:
    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    
    # Extract the environment name from its path
    env_name = os.path.basename(sys.prefix)
    print(f"Virtual Environment: {env_name}")

    # Show the root path of the current environment
    print(f"Environment Path: {sys.prefix}\n")

    print(
        "SUCCESS: You're in an isolated environment!",
        "Safe to install packages without affecting",
        "the global system.\n",
        sep="\n"
    )
    print("Package installation path:")
    # Get the directories where Python installs packages
    paths = site.getsitepackages()
    for path in paths:
        print(path)