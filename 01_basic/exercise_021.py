number = int(input("Choose a number: "))

result = "odd"
if number % 2 == 0:
    result = "even"

print("Your number is %s" % result)