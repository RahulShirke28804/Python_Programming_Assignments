'''
    Q3) Display File Line by Line
    Problem Statement:
    Write a program which accepts a file name from the user and displays the contents of the file line by line on the
    screen.
    
    Input:
    Demo.txt
    
    Expected Output:
    Display each line of Demo.txt one by one.
'''

def DisplayLineByLine(FileName):
    fd = open(FileName, "r")

    Buffer = fd.readline()
    
    while(len(Buffer) > 0): 
        print(Buffer)
        Buffer = Buffer = fd.readline()


def main():
    Filename = input("Enter the name of the file : ")

    print("Contents of the file ", Filename, " are : ")
    DisplayLineByLine(Filename)


if __name__ == "__main__":
    main()
