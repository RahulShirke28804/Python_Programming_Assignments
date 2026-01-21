'''
    2.Write a program which accepts one number and prints count of digits in that number.
    Input: 7521
    Output: 4

'''

def CountDigits(No):
    Count = 0

    if(No < 0):
        No = -No

    while(No != 0):
        No = No // 10
        Count = Count + 1

    return Count

def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")
    Value = int(input())

    Ret = CountDigits(Value)

    print("Number  of digits in",Value,"are : ",Ret)
    
if __name__ == "__main__":
    main()
