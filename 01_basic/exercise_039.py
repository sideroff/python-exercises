def main():
    principal = float(input("Choose a number(principal): "))
    interest = float(input("Choose another number(interest): "))
    years = float(input("Choose another number(years): "))

    return print("Simple interest = A = P(1 + rt) = %.2f" % ( principal*(1 + 0.01*interest*years) ))

if __name__ == '__main__': main()