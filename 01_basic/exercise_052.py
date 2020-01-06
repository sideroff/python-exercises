from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
    eprint("abc", "efg", "xyz", sep="--")

if __name__ == '__main__': main()