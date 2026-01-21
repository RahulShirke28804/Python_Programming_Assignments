'''
    3. Write a program which accepts one number and prints sum of digits.
    Input: 123
    Output: 6

'''

def SumDigits(No):
    Digit = 0
    Sum = 0

    if(No < 0):
        No = -No

    while(No != 0):
        Digit = No % 10
        No = No // 10
        Sum = Sum + Digit

    return Sum

def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")
    Value = int(input())

    Ret = SumDigits(Value)

    print("Sum of all rhe digits in",Value,"are : ",Ret)
    
if __name__ == "__main__":
    main()
