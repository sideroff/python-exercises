from math import sqrt

def main():
    height = float(input("Input your height in meters: "))
    weight = float(input("Input your weight in kilogram: "))
    print("Your body mass index is: ", round(weight / (height * height), 2))

if __name__ == '__main__': main()