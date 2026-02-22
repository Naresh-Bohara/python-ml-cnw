## encapsulation: Encapsulation is the process of hiding the internal details of an object and only exposing a public interface. This is done to protect the internal state of the object from being modified by external code. In Python, we can achieve encapsulation by using private attributes and methods. Private attributes and methods are defined with a double underscore prefix (__) and are not accessible from outside the class. However, they can still be accessed from within the class using the self keyword. Encapsulation helps to improve code maintainability and reduces the risk of unintended side effects by preventing external code from directly modifying the internal state of an object.

# - achieved via access control (private, protected, public)
# - private members are not accessible outside the class
# - protected members are accessible within the class and its subclasses
# - public members are accessible from anywhere

class Bank:
    def __init__(self):
        self.__balance = 1000  # private attribute
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def show_balance(self):
        print(f"Current balance: {self.__balance}")

account = Bank()
account.deposit(500)    # Output: Deposited: 500. New balance:
account.show_balance()  # Output: Current balance: 1500
account.withdraw(200)   # Output: Withdrew: 200. New balance: 1300
account.show_balance()  # Output: Current balance: 1300
