from math import sqrt

def main():
    arm_one = float(input("Arm one length: "))
    arm_two = float(input("Arm two length: "))

    print("The hypotenuse of a triangle with arm one: %.2f and arm two: %.2f is: %.2f" % (arm_one, arm_two, sqrt(arm_one**2 + arm_two**2) ))

if __name__ == '__main__': main()