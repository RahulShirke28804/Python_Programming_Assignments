'''
    3. Write a program which accepts one number and prints square of that number.
    Input: 5
    Output: 25
'''
def Square(No1):
    return No1 * No1

def main():
    iRet = 0
    Value1 = int(input("Enter number : "))

    iRet = Square(Value1)

    print("Square is : ",iRet)

if __name__ == "__main__":
    main()
