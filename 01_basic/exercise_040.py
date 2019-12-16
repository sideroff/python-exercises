from math import sqrt

def main():
    x1 = float(input("Choose a number(x1): "))
    y1 = float(input("Choose another number(y1): "))
    x2 = float(input("Choose a number(x2): "))
    y2 = float(input("Choose another number(y2): "))

    return print("distance between the 2 points is = %.2f" % ( sqrt(pow(x1-x2, 2) + pow(y1-y2, 2)) ))

if __name__ == '__main__': main()