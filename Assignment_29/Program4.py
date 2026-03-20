'''
    Q4) Compare Two Files (Command Line)
    Problem Statement:
    Write a program which accepts two file names through command line arguments and compares the contents of
    both files.
    • If both files contain the same contents, display Success
    • Otherwise display Failure
    
    Input (Command Line):
    Demo.txt Hello.txt
    
    Expected Output:
    Success OR Failure
'''
import sys
import hashlib

def Checksum(Filename):
    try:
        fd = open(Filename,"rb")
        
        hashvalue = hashlib.md5()

        Buffer = fd.read(1024)

        while(len(Buffer) > 0):
            hashvalue.update(Buffer)
            Buffer = fd.read(1024)
    
    except FileNotFoundError:
        print("Unable to open file as there is no such file")
        return
    
    return hashvalue.hexdigest()

def main():
    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        return
        
    srcRet = Checksum(sys.argv[1])
    destRet = Checksum(sys.argv[2])

    if(srcRet == destRet):
        print("Success")

    else:
        print("Failure")

if __name__ == "__main__":
    main()
    

