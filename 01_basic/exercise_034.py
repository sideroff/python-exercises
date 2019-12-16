def main():
    input_int = float(input("Choose a number(1): "))
    input_int2 = float(input("Choose another number(2): "))
    int_sum = sum([input_int, input_int2])
    
    if int_sum >=15 and int_sum <= 20: return print("sum is between 15 and 20 => returning 20")
    return print("sum= %.2f" %(int_sum))

if __name__ == '__main__': main()