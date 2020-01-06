from time import time

def main():
    for i in range(1, 1_000_000): 1+1

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print("main method executed in %fs" % (end-start))