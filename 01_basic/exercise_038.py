def main():
    a = float(input("Choose a number(a): "))
    b = float(input("Choose another number(b): "))

    return print("(a+b)^2 = a^2 + 2ab + b^2 = %.2f" %(a**2 + 2*a*b + b**2))

if __name__ == '__main__': main()