import sys

if sys.version_info:
    print(".".join(map(lambda x: str(x), sys.version_info)))
else:
    print("No version info available.")