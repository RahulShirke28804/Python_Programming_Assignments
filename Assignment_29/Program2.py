'''
    Q2) Display File Contents
    Problem Statement:
    Write a program which accepts a file name from the user, opens that file, and displays 
    the entire contents on the console.

    Input:
    Demo.txt
    
    Expected Output:
    Display contents of Demo.txt on console.
'''

def main():
    fd = 0

    print("Enter the name of file that you want to read : ")
    Filename = input()

    try:
        fd = open(Filename,"r")

        Data = fd.read()
    
        print("Data from the file is : \n",Data)

        fd.close()

    except FileNotFoundError:
        print("File not found as there is no such file")

if __name__ == "__main__":
    main()
    

