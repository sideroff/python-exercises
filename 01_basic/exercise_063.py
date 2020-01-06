from os.path import abspath, dirname, join

def main():
    print(join(abspath(dirname(__file__)), __file__[2::]  ))

if __name__ == '__main__': main()