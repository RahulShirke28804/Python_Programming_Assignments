'''
    3: Write a Python program to implement a class named Arithmetic with the following characteristics:
        • The class should contain two instance variables: Value1 and Value2.
        • Define a constructor (__init__) that initializes all instance variables to 0.
        • Implement the following instance methods:
            ◦ Accept() : accepts values for Value1 and Value2 from the user.
            ◦ Addition() : returns the addition of Value1 and Value2.
            ◦ Subtraction() : returns the subtraction of Value1 and Value2.
            ◦ Multiplication() : returns the multiplication of Value1 and Value2.
            ◦ Division() : returns the division of Value1 and Value2 (handle division by zero
            properly).

        • Create multiple objects of the Arithmetic class and invoke all the instance methods.

'''

class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        print("Enter first number : ")
        self.Value1= float(input())
        print("Enter second number : ")
        self.Value2 = float(input())

    def Addition(self):
        Ans = 0.0
        Ans = self.Value1 + self.Value2
        return Ans

    def Subtraction(self):
        Ans = 0.0
        Ans = self.Value1 - self.Value2
        return Ans

    def Multiplication(self):
        Ans = 1
        Ans = self.Value1 * self.Value2
        return Ans

    def Division(self):
        if(self.Value2 == 0):
            return 0
        
        Ans = 0.0
        Ans = self.Value1 / self.Value2
        return Ans


def main():
    Ret = 0.0

    obj1 = Arithmetic()
    obj1.Accept()
   
    Ret = obj1.Addition()
    print("Addition is : ",Ret)
    Ret = obj1.Subtraction()
    print("Subtraction is : ",Ret)
    Ret = obj1.Multiplication()
    print("Multiplication is : ",Ret)
    Ret = obj1.Division()
    print("Division is : ",Ret)
    
    obj2 = Arithmetic()
    obj2.Accept()
   
    Ret = obj2.Addition()
    print("Addition is : ",Ret)
    Ret = obj2.Subtraction()
    print("Substraction is : ",Ret)
    Ret = obj2.Multiplication()
    print("Multiplication is : ",Ret)
    Ret = obj2.Division()
    print("Division is : ",Ret)
      

if __name__ == "__main__":
    main()