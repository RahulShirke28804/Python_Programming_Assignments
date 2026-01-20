'''
    4. Write a program which accepts one number and prints cube of that number.
'''

def Cube(No):
    return No ** 3

def main():
    iRet = 0
    Value = int(input("Enter number : "))

    iRet = Cube(Value)

    print("Cube is : ",iRet)

if __name__ == "__main__":
    main()
