'''
    Q5) Frequency of a String in File
    Problem Statement:
    Write a program which accepts a file name and one string from the user and returns the frequency (count of
    occurrences) of that string in the file.
    
    Input:
    Demo.txt Marvellous
    
    Expected Output:
    Count how many times "Marvellous" appears in Demo.txt.
'''

import sys


def main():
    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        return
    
    try:
        fd = open(sys.argv[1],"r")

        Buffer = fd.read(1024)

        while(len(Buffer) > 0):
            freq = Buffer.count(sys.argv[2])
            Buffer = fd.read(1024)

        fd.close()

    except FileNotFoundError:
        print("File not found as there is no such file")

    print("Frequency of ",sys.argv[2]," is : ",freq)

if __name__ == "__main__":
    main()
    