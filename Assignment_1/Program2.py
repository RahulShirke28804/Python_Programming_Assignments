'''
    2. Write a program which contains one function ChkGreater() that accepts two numbers
        and prints the greater number.
        Input: 10 20
        Output: 20 is greater
'''
def ChkGreater(No1,No2):
    if(No1 > No2):
        return No1
    else:
        return No2

def main():
    iRet = 0
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    iRet = ChkGreater(Value1,Value2)

    print("Greater number is : ",iRet)

if __name__ == "__main__":
    main()