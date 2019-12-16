def main():
    input_int = float(input("Choose a number(1): "))
    input_int2 = float(input("Choose another number(2): "))
    input_int3 = float(input("Choose another number(3): "))

    int_set = set([input_int,input_int2, input_int3])
    if len(int_set) == 2: return print("2 equal values provided => sum= 0")
    return print("sum= %.2f" %(sum(int_set)))

if __name__ == '__main__': main()