'''
    2. Write a program which accepts radius of circle and prints area of circle.

'''

from math import pi

def CircleArea(rad):
    Area = 0

    Area = pi * rad * rad

    return Area

def main():
    Radius = 0.0
    Ret = 0.0
    
    print("Enter the radius of circle : ")
    Radius = float(input())

    Ret = CircleArea(Radius)

    print("Area of Circle is :", Ret)

if __name__ == "__main__":
    main()
