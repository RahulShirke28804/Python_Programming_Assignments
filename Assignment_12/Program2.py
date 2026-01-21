'''
    2. Write a program which accepts one number and prints its factors.
    Input: 12
    Output: 1 2 3 4 6 12

'''


def DisplayFactors(No):

    for i in range(1,(No//2)+1):
        if((No % i) == 0):
            print(i,end=" ")

    print(No)

    
def main():
    Value = 0

    print("Enter the number : ")
    Value = int(input())

    DisplayFactors(Value)

if __name__ == "__main__":
    main()