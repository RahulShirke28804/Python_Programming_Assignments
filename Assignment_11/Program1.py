'''
    1. Write a program which accepts one number and checks whether it is prime or not.
    Input: 11
    Output: Prime Number

'''

def ChkPrime(No):
    bFlag = False

    for i in range(2,(int)(No/2)+1):
        if((No % i) == 0):
            bFlag = True
            break

    return bFlag

def main():
    Value = 0
    Ret = False

    print("Enter the number : ")
    Value = int(input())

    Ret = ChkPrime(Value)

    if(Ret == False):
        print(Value,"is Prime Number")

    else:
        print(Value,"is Not a Prime Number")

if __name__ == "__main__":
    main()
