'''
    Q1) Count Lines in a File
    Problem Statement:
    Write a program which accepts a file name from the user and counts how many lines are present in the file.
    
    Input:
    Demo.txt
    
    Expected Output:
    Total number of lines in Demo.txt.
'''

def CountLines(FileName):
    fd = open(FileName, "r")

    iRet = fd.readlines()

    return len(iRet)

def main():
    iRet = 0

    Filename = input("Enter the name of the file : ")

    iRet = CountLines(Filename)

    print("Number of lines in the file are : ", iRet)

if __name__ == "__main__":
    main()
