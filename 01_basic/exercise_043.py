from os import name
from platform import system, release

print("Python is running on %s %s platform, version %s" % ( system(), name, release() ))