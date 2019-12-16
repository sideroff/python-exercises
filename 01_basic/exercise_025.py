list_input = list(input("Choose a list of numbers separated by ', ': ").split(", "))

value_input = input("Choose a value to look for in the provided list: ")

print("Value is %spresent in list." % ("" if value_input in list_input else "not "))