'''
    Q3) Copy File Contents into a New File (Command Line)
    Problem Statement:
    Write a program which accepts an existing file name through command line arguments, creates a new file
    named Demo.txt, and copies all contents from the given file into Demo.txt.
    
    Input (Command Line):
    ABC.txt
    
    Expected Output:
    Create Demo.txt and copy contents of ABC.txt into Demo.txt.
'''
import sys

def main():

    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        return
        
    try:
        srcfd = open(sys.argv[1],"r")

        Data = srcfd.read()
    
        destfd = open("Demo.txt", "w")

        destfd.write(Data)

        srcfd.close()

        destfd.close()

    except FileNotFoundError:
        print("File not found as there is no such file")

if __name__ == "__main__":
    main()
    

