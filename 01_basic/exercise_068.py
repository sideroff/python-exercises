from math import sqrt

def main():
    digit = int(input("Choose an int: "))

    sum_of_digits = sum(list(map(int, list(str(digit)))))

    print("The sum of the digits in %i is %i" % (digit, sum_of_digits))

if __name__ == '__main__': main()