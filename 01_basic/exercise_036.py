def main():
    input_int = input("Choose a number(1): ")
    input_int2 = input("Choose another number(2): ")

    if represents_int(input_int) and represents_int(input_int2): 
        return print("Both values are ints. sum= %i" %(int(input_int) + int(input_int2)))
    return print("One or more of the values is not an integer")

def represents_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__': main()