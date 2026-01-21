'''
    4. Write a program which accepts one number and prints reverse of that number.
    Input: 123
    Output: 321

'''

def SumDigits(No):
    Digit = 0
    Reverse = 0
    nums = No

    if(nums < 0):
        nums = -No

    while(nums != 0):
        Digit = nums % 10
        Reverse = ((Reverse * 10) + Digit)
        nums = nums // 10

    if(No < 0):
        return -Reverse

    else:
        return Reverse        


def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")
    Value = int(input())

    Ret = SumDigits(Value)

    print("Reverse digits of",Value,"is : ",Ret)
    
if __name__ == "__main__":
    main()
