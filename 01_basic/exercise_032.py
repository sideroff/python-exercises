from exercise_031 import euclidian_gcd

input_int = float(input("Choose a number: "))
input_int2 = float(input("Choose another number: "))


print("lcm = %.0f" % ((input_int*input_int2)/euclidian_gcd(input_int, input_int2)))