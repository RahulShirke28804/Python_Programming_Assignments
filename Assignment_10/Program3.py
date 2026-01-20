'''
    3. Write a program which accepts one number and prints factorial of that number.
    Input: 5
    Output: 120

'''

def Factorial(No):
    Fact = 1

    if(No < 0):         # Updater
        print("Invalid input!")
        return -1

    for i in range(1,No+1):
        Fact = Fact * i

    return Fact

def main():
    iRet = 0

    print("Enter the number : ")
    Value = int(input())

    iRet = Factorial(Value)

    if(iRet > 0):
        print("Factorial of ",Value,"is : ",iRet)
    
if __name__ == "__main__":
    main()
