'''
    5.Write a program which accepts one number and prints all odd numbers till that number.
'''

def DisplayOdd(No):
    if(No <= 0):         # Updater
        print("Invalid input!")
        return -1

    print("Odd numbers are :")
    for i in range(1,No+1,2):
        print(i,"\t")

def main(): 
    print("Enter the number : ")
    Value = int(input())

    DisplayOdd(Value)

if __name__ == "__main__":
    main()
