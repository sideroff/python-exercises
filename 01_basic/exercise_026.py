int_list_input = list(map(int, input("Choose a list of ints seperated by ', ': ").split(", ")))

for num in int_list_input:
    print("@"*num)