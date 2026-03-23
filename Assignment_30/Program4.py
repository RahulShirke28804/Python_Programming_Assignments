'''
    Q4) Copy File Contents into Another File
    Problem Statement:
    Write a program which accepts two file names from the user.
    • First file is an existing file
    • Second file is a new file
    Copy all contents from the first file into the second file.
    
    Input:
    ABC.txt Demo.txt

    Expected Output:
    Contents of ABC.txt copied into Demo.txt.
'''
import sys

def CopyContents():
    srcfd = None
    destfd = None

    srcfd = open(sys.argv[1], "r")
    if(srcfd == None):
        print("Unable to open file")
        return
    
    destfd = open(sys.argv[2], "w")
    if(destfd == None):
        print("Unable to create destination file")
        srcfd.close()
        return
    
    Buffer = srcfd.read()

    while(len(Buffer) > 0):
        destfd.write(Buffer)
        Buffer = srcfd.read(len(Buffer))



def main():
    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        return
    
    CopyContents()


if __name__ == "__main__":
    main()
    

