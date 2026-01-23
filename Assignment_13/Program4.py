'''
    4. Write a program which accepts one number and prints binary equivalent.

'''

def Binary(No):
    binary = list()
    
    while(No != 0):
        if((No % 2) == 0):
            binary.append(0)
        else:
            binary.append(1)

        No = No // 2

    return binary

def main(): 
    Value = 0

    print("Enter the number : ")
    Value = int(input())

    Binary(Value)

    ret = Binary(Value)

    for i in range(len(ret) - 1, -1 ,-1):
        print(ret[i],end=" ")

if __name__ == "__main__":
    main()
