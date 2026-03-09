#!/usr/bin/env python
import sys
import subprocess
try:
    import importlib.metadata as metadata
except ImportError:
    # This acts as the fallback for Python 3.7
    import importlib_metadata as metadata 

def check_pkg(name):
    try:
        version = metadata.version(name)
        print(f"FOUND: {name} (version {version})")
        return True
    except metadata.PackageNotFoundError:
        print(f"MISSING: {name}")
        return False

print("\n--- Diagnostic Check ---")
required = ['rpy2', 'numpy', 'pysam']
all_found = all([check_pkg(p) for p in required])

# Check external CLI tools
r_check = subprocess.run(["R", "--version"], capture_output=True)
sam_check = subprocess.run(["samtools", "--version"], capture_output=True)

if not all_found or r_check.returncode != 0 or sam_check.returncode != 0:
    print("\nERROR: Missing dependencies or CLI tools failed.")
    sys.exit(1) # This tells conda-build the test failed

print("\nGreat job! All dependencies found.")
sys.exit(0)
