'''
    5. Write a program which accepts marks and displays grade.
    Condition Example:
    • ≥ 75 → Distinction
    • ≥ 60 → First Class
    • ≥ 50 → Second Class
    • < 50 → Fail

'''

def DisplayGrade(No):

    if(No > 100 or No < 0):
        print("Invalid marks!!")
        return
    
    if(No >= 75):
        print("Distinction")

    elif(No >= 60 and No < 75):
        print("First Class")

    elif(No >= 50 and No < 60):
        print("Second Class")

    elif(No <50):
        print("Fail")

def main(): 
    print("Enter the number : ")
    Value = int(input())

    DisplayGrade(Value)

if __name__ == "__main__":
    main()
