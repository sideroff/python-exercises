from math import sqrt

def main():
    [feet, rest] = input("height (eg. 5'9\"): ").split("'")
    inches = rest.split('"')[0]

    feet = float(feet)
    inches = float(inches)

    print("%.2f feet, %.2f inches = %.2fcm" % (feet, inches, ((feet * 12) + inches) * 2.54 ))

if __name__ == '__main__': main()