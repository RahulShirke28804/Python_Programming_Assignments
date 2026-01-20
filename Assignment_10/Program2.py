'''
    2. Write a program which accepts one number and prints sum of first N natural numbers.
    Input: 5
    Output: 15

'''

def Summation(No):
    Sum = 0

    if(No < 0):         # Updater
        No = -No

    for i in range(1,No+1):
        Sum = Sum + i

    return Sum
def main():
    iRet = 0
    print("Enter the number : ")
    Value = int(input())

    iRet = Summation(Value)

    print("Summation of first ",Value,"numbers is : ",iRet)

if __name__ == "__main__":
    main()
