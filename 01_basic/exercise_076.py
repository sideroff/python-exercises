import sys

def main():
    print("This is the name/path of the script:"),sys.argv[0]
    print("Number of arguments:",len(sys.argv))
    print("Argument List:",str(sys.argv))
    
if __name__ == '__main__': main()