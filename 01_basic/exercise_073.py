from math import sqrt

def main():
    line_one = list(map(lambda x: float(x.strip()), input("Line 1 x,y: ").split(",")))
    line_two = list(map(lambda x: float(x.strip()), input("Line 2 x,y: ").split(",")))

    mid_point = ((line_one[0] + line_two[0]) / 2, (line_one[1] + line_two[1]) / 2)

    print(mid_point)
if __name__ == '__main__': main()