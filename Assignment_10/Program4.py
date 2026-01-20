'''
    4. Write a program which accepts one number and prints all even numbers till that number.
    Input: 10
    Output: 2 4 6 8 10
'''

def DisplayEven(No):
    if(No < 0):         # Updater
        print("Invalid input!")
        return -1

    print("Even numbers are :")
    for i in range(2,No+1,2):
        print(i,"\t")

def main(): 
    print("Enter the number : ")
    Value = int(input())

    DisplayEven(Value)

if __name__ == "__main__":
    main()
