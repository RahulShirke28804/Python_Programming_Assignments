'''
    1. Write a program which accepts one number and prints multiplication table of that
    number.
    Input: 4
    Output:
    4 8 12 16 20 24 28 32 36 40

'''

def Table(No):
    print("Table of",No)
    for i in range(1,11):
        print(No * i,"\t")
    
def main():
    print("Enter the number : ")
    Value = int (input())

    Table(Value)

if __name__ == "__main__":
    main()
