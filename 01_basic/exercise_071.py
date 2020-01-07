import glob
import os

def main():
    files = glob.glob("*.py")
    files.sort(key=os.path.getctime)
    print("\n".join(files))
    
if __name__ == '__main__': main()