'''
    1. Write a program which accepts one character and checks whether it is vowel or
    consonant.
    Input: a
    Output: Vowel

'''

def ChkVowel(Character):
    bFlag = False

    if(Character == 'a' or Character == 'e' or Character == 'i' or Character == 'o' or Character == 'u' or Character == 'A' or Character == 'E' or Character == 'I' or Character == 'O' or Character == 'U'):
        return True
    
    else:
        return False

def main():
    Value = 0
    Ret = False

    print("Enter the character : ")
    Value = input()

    Ret = ChkVowel(Value)

    if(Ret == True):
        print(Value,"is a Vowel")
    else:
        print(Value,"is a Consonant")


if __name__ == "__main__":
    main()
