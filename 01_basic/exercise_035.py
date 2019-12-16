def main():
    input_int = float(input("Choose a number(1): "))
    input_int2 = float(input("Choose another number(2): "))
    int_sum = sum([input_int, input_int2])
    int_dif = abs(input_int - input_int2)
    
    if input_int == input_int2 or int_sum == 5 or int_dif == 5: return print('true')
    return print('false')

if __name__ == '__main__': main()