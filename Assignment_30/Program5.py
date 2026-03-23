'''
    Q5) Search a Word in File
    Problem Statement:
    Write a program which accepts a file name and a word from the user and checks whether that word is present in
    the file or not.
    
    Input:
    Demo.txt Marvellous

    Expected Output:
    Display whether the word Marvellous is found in Demo.txt or not.

'''
import sys

def CountWord():
    fd = None
    bFlag = False

    fd = open(sys.argv[1],"r")
    if(fd == None):
        print("Unable to open file")
        return
    
    buffer = fd.readline()

    while(buffer != ""):
        
        for word in buffer.split():
            if(word == sys.argv[2]):
                bFlag = True
                break
            
        buffer = fd.readline()
            

    
    return bFlag


def main():
    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        return
    
    bRet = False

    bRet = CountWord()

    if(bRet == True):
        print(sys.argv[2],"Word found")
    else:
        print(sys.argv[2],"Word not found")
        

if __name__ == "__main__":
    main()