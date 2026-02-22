from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, balance, name):
        self.__balance = balance
        self.name = name

    # Getter(Encapsulation)
    def get_balance(self):
        return self.__balance

    # Setter(Encapsulation)
    def set_balance(self, amount):
        self.__balance = amount

    def deposite(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    # Abstraction
    @abstractmethod
    def calculate_interest(self):
        pass


# inheritace + polymorphism
class SavingAccount(Account):
    def calculate_interest(self):
        interest = self.get_balance() * 0.05  # 5% interest rate
        print(f"Saving Account interest: {interest}")


class CurrentAccount(Account):
    def calculate_interest(self):
        interest = self.get_balance() * 0.03  # 3% interest rate
        print(f"Saving Account interest: {interest}")


# creating objects

s = SavingAccount(10000, "Ram")
c = CurrentAccount(15000, "Shyam")


print("-------Saving account-----")
s.deposite(2000)
s.withdraw(3000)
print(f"Balance:{s.get_balance()}")
s.calculate_interest()


print("-------Current account-----")
c.deposite(1000)
c.withdraw(5000)
print(f"Balance:{c.get_balance()}")
c.calculate_interest()
