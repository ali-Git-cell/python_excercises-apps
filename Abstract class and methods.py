# Import ABC and abstractmethod from the module abc (which stands for abstract base classes)
from abc import ABC, abstractmethod

# Class Bank
class Bank(ABC):

    def basicinfo():
        print("This is a generic back")
        return "Generic back: 0"
    @abstractmethod
    def withdraw():
        pass

# Class Swiss
class Swiss(Bank):
    
    bal = 1000 
    def basicinfo(self):
        print("This is the Swiss Bank")
        return "Swiss Bank: {}".format(self.bal)

    def withdraw(self, amount):
        if self.bal < amount:
            print("Insufficient funds")
            return self.bal
        else: 
            self.bal -= amount
            print("Withdrawn amount: {}".format(amount))
            print("New balance: {}".format(self.bal))
            return self.bal
   
# Driver Code
def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1000)

if __name__ == "__main__":
    main()