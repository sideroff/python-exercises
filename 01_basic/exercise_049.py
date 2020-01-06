from os import listdir
from os.path import isfile, join

def main():
    input_path = input("Choose a dir: ")

    print("Files in %s:\n\t%s" % ( input_path, "\n\t".join((f for f in listdir(input_path) if isfile(join(input_path,f) )))))

if __name__ == '__main__': main()