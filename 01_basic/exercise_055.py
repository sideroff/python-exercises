from socket import gethostbyname, gethostname

def main():
    print(gethostbyname(gethostname()))

if __name__ == '__main__': main()