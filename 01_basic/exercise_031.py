def euclidian_gcd(num1: float, num2: float):
    return num1 if num2 == 0 else euclidian_gcd(num2, num1 % num2) 

def main():
    input_int = float(input("Choose a number: "))
    input_int2 = float(input("Choose another number: "))
    
    if input_int < input_int2:
        temp = input_int
        input_int = input_int2
        input_int2 = temp

    print("gcd = %.0f" % (euclidian_gcd(input_int, input_int2)))


if __name__ == '__main__':
    main()