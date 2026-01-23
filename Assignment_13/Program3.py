'''
    3. Write a program which accepts one number and checks whether it is perfect number or not.
    Input: 6
    Output: Perfect Number
'''

def ChkPerfect(No):
    Sum = 0

    for i in range(1,(No//2)+1):
        if((No % i) == 0):
            Sum = Sum + i

    print(Sum)
    if(Sum == No):
        return True
    else:
        return False

def main():
    Value = 0
    Ret = False

    print("Enter the number : ")
    Value = int(input())

    Ret = ChkPerfect(Value)

    if(Ret == True):
        print(Value,"is perfect Number")

    else:
        print(Value,"is Not a perfect Number")

if __name__ == "__main__":
    main()
