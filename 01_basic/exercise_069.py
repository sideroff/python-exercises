def main():
    digit_one = float(input("Digit one: "))
    digit_two = float(input("Digit two: "))
    digit_three = float(input("Digit three: "))

    digit_list = [digit_one, digit_two, digit_three]

    digit_list.sort()

    print(digit_list)

if __name__ == '__main__': main()