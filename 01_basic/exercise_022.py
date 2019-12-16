split_input = input("Provide a list of numbers: ").split(", ")
print(len(list(filter(lambda x: (x == 4),map(float, list(split_input))))))