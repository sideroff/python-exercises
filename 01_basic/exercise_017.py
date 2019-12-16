number = float(input("Choose a number: "))

numbers = [1000, 2000, 3000]
value = ", ".join(map(str, numbers[:-1])) + " and %i" % numbers[-1]
result = "Your number is more than 100 away from %s" % (value)


for num in numbers:
    if (abs(num - number) < 100):
        result = "Your number is less than 100 away from %.2f" % (num)

print(result)