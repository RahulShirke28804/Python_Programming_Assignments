'''
    5. Write a program which accepts one number and checks whether it is palindrome or not.
    Input: 121  
    Output: Palindrome  

'''

def ChkPalindrome(No):
    Digit = 0
    Reverse = 0
    nums = No
    
    if(No < 0):
        return False

    while(nums != 0):
        Digit = nums % 10
        Reverse = ((Reverse * 10) + Digit)
        nums = nums // 10

    if(No == Reverse):
        return True
    else:
        return False


def main():
    Value = 0
    Ret = False

    print("Enter the number : ")
    Value = int(input())

    Ret = ChkPalindrome(Value)

    if(Ret == True):
        print(Value,"is a Palindrome")
    else:
        print(Value,"is not a Palindrome")

if __name__ == "__main__":
    main()
