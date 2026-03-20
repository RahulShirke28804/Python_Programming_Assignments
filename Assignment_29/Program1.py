'''
    Q1) Check File Exists in Current Directory
    Problem Statement:
    Write a program which accepts a file name from the user and checks whether that file exists in the current
    directory or not.

    Input:
    Demo.txt
    
    Expected Output:
    Display whether Demo.txt exists or not.
'''
import os

def IfFileExists(filename):
    Flag = False

    Current_Directory = os.getcwd()

    for Folder, SubFolder, Filename in os.walk(Current_Directory):
        for name in Filename:
            if(name == filename):
                Flag = True
                break
        break
    
    return Flag 

def main():
    Ret = False

    print("Enter the name of file : ")

    FileName = input()

    Ret = IfFileExists(FileName)

    if(Ret == True):
        print("File is present the the current dierctory")
    else:    
        print("File is not present the the current dierctory")

if __name__ == "__main__":
    main()
