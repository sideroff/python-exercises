from math import sqrt

def main():
    feet = float(input("feet: "))
    print("""
    %f feet is equal to:
    %f inches,
    %f yards,
    %f miles,
    """ % (feet, feet * 12, feet * 0.333333, feet * 0.000189394 ))

if __name__ == '__main__': main()