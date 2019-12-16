number = float(input("Your number: "))

result = 17 - number

if (number > 17):
    result = abs(number - 17)*2

print("Difference: %.2f" % result)