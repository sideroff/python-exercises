def substring_occurances(str_arg, n = 0):
    if n < 2:
        print("Integer < 2 passed. Your string multiplied by it is: %s" % str_arg*n )
        return
    print("The substring %s copied %i times is %s" % (str_arg[:2], n, str_arg[:2]*n))

string_input = input("Choose a string: ")
int_input = int(input("Choose a number: "))

substring_occurances(string_input, int_input)
