numbers = list(map(float, input("Choose numbers ( separated by ', ' ): ").split(', ')))

print(numbers)
num_sum = sum(numbers)
result = num_sum

if (num_sum == len(numbers)):
    result = len(numbers) * num_sum

print("Sum is: %.2f" % result)