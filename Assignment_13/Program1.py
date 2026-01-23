'''
    1. Write a program which accepts length and width of rectangle and prints area.

'''

def RecArea(Length, Width):
    Area = 0

    Area = Length * Width

    return Area

def main():
    length = 0.0
    width = 0.0
    Ret = 0.0

    print("Enter the length of rectangle : ")
    length = float(input())

    print("Enter the width of rectangle : ")
    width = float(input())

    Ret = RecArea(length, width)

    print("Area of rectangle is :", Ret)


if __name__ == "__main__":
    main()
