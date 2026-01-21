'''
    5. Write a program which accepts one number and prints that many numbers in reverse
    order.
    Input: 5
    Output: 5 4 3 2 1
'''

def ReverseDisplay(No):
    for i in range(No,0,-1):
        print(i,end = " ")

    print()

def main(): 
    print("Enter the number : ")
    Value = int(input())

    ReverseDisplay(Value)

if __name__ == "__main__":
    main()