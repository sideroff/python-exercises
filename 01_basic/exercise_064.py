from os.path import getmtime, getctime
from datetime import datetime

def main():
    print("File %s was created on %s and last modified on %s" % ( 
      __file__, 
      datetime.fromtimestamp(getctime(__file__)).strftime("%d/%m/%y - %H:%M:%S"),
      datetime.fromtimestamp(getmtime(__file__)).strftime("%d/%m/%y - %H:%M:%S")))


if __name__ == '__main__': main()