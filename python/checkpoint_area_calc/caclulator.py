import math
import sys

print("""
==================
Area Calculator 📐
==================

1) Triangle
2) Rectangle
3) Square
4) Circle
5) Quit
""")

def calculate_area(method):
    if method == 5:
        return sys.exit()
    elif method == 4:
        #calculate area of circle
        radius = int(input("Enter radius: "))
        return radius * math.pi
    elif method == 3:
        side = int(input("Enter side length: "))
        return side * side
    elif method == 2:
        #rectangle
        height = int(input("Enter height: "))
        length = int(input("Enter length: "))
        return height * length
    elif method == 1:
        base_side = int(input("Enter base side: "))
        height = int(input("Enter height: "))
        return base_side * height / 2
        #triangle

if __name__ == "__main__":
    method = int(input("Which shape: "))
    print(calculate_area(method))