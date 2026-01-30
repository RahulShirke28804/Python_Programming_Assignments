'''
    3: Write a Python program to implement a class named Numbers with the following specifications:
        • The class should contain one instance variable:
            ◦ Value
        • Define a constructor (__init__) that accepts a number from the user and initializes Value.
        • Implement the following instance methods:
            ◦ ChkPrime() : returns True if the number is prime, otherwise returns False
            ◦ ChkPerfect() : returns True if the number is perfect, otherwise returns False
            ◦ Factors() : displays all factors of the number
            ◦ SumFactors() : returns the sum of all factors
            (You may use this method as a helper in ChkPerfect() if required)

        • Create multiple objects and call all methods.

'''

class Numbers:

    def __init__(self,no):
        self.Value = no

    def ChkPrime(self):
        if(self.Value == 1):
            return False
        
        for i in range(2,(self.Value // 2) + 1):
            if((self.Value % i) == 0):
                break

        if(i == self.Value // 2):
            return True
        else:
            return False

    def SumFactor(self):
        Sum = 0
        for i in range(1,(self.Value // 2)+1):
            if((self.Value % i) == 0):
                Sum = Sum + i
        return Sum
    
    def ChkPerfect(self):
        Sum = 0
        for i in range(1,(self.Value // 2)+1):
            if((self.Value % i) == 0):
                Sum = Sum + i

        if(Sum == self.Value):
            return True
        else:
            return False
        
    def Factor(self):
        print(f"Factors of {self.Value} are : ")
        
        for i in range(1,(self.Value // 2)+1):
            if((self.Value % i) == 0):
                print(i,end=" ")

def main():
    Ret = False

    print("Enter the number : ",end=" ")
    no1 = int(input())   

    obj1 = Numbers(no1)

    Ret = obj1.ChkPrime()
    if(Ret == True):
        print(no1,"is a prime number")
    else:
        print(no1,"is not a prime number")

    Ret = obj1.SumFactor()
    print(f"Sum of factors of {no1} is : ",Ret)

    Ret = obj1.ChkPerfect()
    if(Ret == True):
        print(no1,"is a perfect number")
    else:
        print(no1,"is not a perfect number")

    print("Enter the number : ",end=" ")
    no2 = int(input())   

    obj2 = Numbers(no2)

    Ret = obj2.ChkPrime()
    if(Ret == True):
        print(no1,"is a prime number")
    else:
        print(no1,"is not a prime number")

    Ret = obj2.SumFactor()
    print(f"Sum of factors of {no1} is : ",Ret)

    Ret = obj2.ChkPerfect()
    if(Ret == True):
        print(no1,"is a perfect number")
    else:
        print(no1,"is not a perfect number")

if __name__ == "__main__":
    main()