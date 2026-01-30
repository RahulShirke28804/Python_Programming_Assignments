'''
    2: Write a Python program to implement a class named BankAccount with the following requirements:
        • The class should contain two instance variables:
            ◦ Name (Account holder name)
            ◦ Amount (Account balance)
        • The class should contain one class variable:
            ◦ ROI (Rate of Interest), initialized to 10.5
        • Define a constructor (__init__) that accepts Name and initial Amount.
        • Implement the following instance methods:
            ◦ Display() : displays account holder name and current balance
            ◦ Deposit() : accepts an amount from the user and adds it to balance
            ◦ Withdraw() : accepts an amount from the user and subtracts it from balance
            (Ensure withdrawal is allowed only if sufficient balance exists)
            ◦ CalculateInterest() : calculates and returns interest using formula:
            Interest = (Amount * ROI) / 100
        • Create multiple objects and demonstrate all methods.

'''

class BankAccount:    
    ROI = 10.5
    
    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount

    def Display(self):
        print(f"Name : {self.Name}\nCurrent balance : {self.Amount}")

    def Deposit(self, amount):
        self.Amount = self.Amount + amount

    def Withdraw(self, amount):
        if(amount > self.Amount):
            print("Insufficient balance")
        else:
            self.Amount = self.Amount - amount
    
    def CalculateInterest(self):
        Interest = (self.Amount * self.ROI) / 100
        return Interest

def main():
    ret = 0

    Obj1 = BankAccount("Rahul",50000)
    Obj1.Display()
    Obj1.Deposit(300)
    Obj1.Display()
    Obj1.Withdraw(500)
    Obj1.Display()
    Ret = Obj1.CalculateInterest()
    print("Rate of intrest is : ",Ret)

    Obj2 = BankAccount("Aditi",300000)
    Obj2.Display()
    Obj2.Deposit(300)
    Obj2.Display()
    Obj2.Withdraw(500)
    Obj2.Display(       )
    Ret = Obj2.CalculateInterest()
    print("Rate of intrest is : ",Ret)

if __name__ == "__main__":
    main()