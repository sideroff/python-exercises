import re

input_string = input("Choose a string: ")

number_value = False
postfix = ""

def main():
    if not re.search("^[\d|\d+\.\d+]+$", input_string):
        print("Provided value is neither a float nor an int.")
        return

    if input_string.count(".") == 1:
        number_value = float(input_string)
    
    if input_string.count(".") == 0:
        number_value = int(input_string)

    print("Provided value is " + str(number_value))

if __name__ == "__main__":
    main()