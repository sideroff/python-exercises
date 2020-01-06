from shutil import get_terminal_size

def main():
    print(get_terminal_size(fallback=(80, 24)))

if __name__ == '__main__': main()