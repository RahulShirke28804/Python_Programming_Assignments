'''
    5. Write a program which accepts one number and checks whether it is divisible by 3 and 5
    Input: 15
    Output: Divisible by 3 and 5
'''
def Divisible(No):
    if((No % 3 == 0) and (No % 5 == 0)):
        print(No,"Is Divisible by 3 and 5")
    else:
        print(No,"Is Divisible not by 3 and 5")

def main():
    print("Enter the number : ")
    Value = int(input())

    Divisible(Value)

if __name__ == "__main__":
    main()
