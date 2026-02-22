from abc import ABC, abstractmethod

# Define the interface for a bank account
class BankAccount(ABC):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    # Getter (Encapsulation)
    def get_balance(self):
        return self.balance

    # Setter (Encapsulation)
    def set_balance(self, amount):
        if amount >= 0:
            self.balance = amount
        else:
            print("Balance cannot be negative.")

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


# Implement the interface for a savings account
class SavingsAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")


# Implement the interface for a current account
class CurrentAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")


# Example usage
savings_account = SavingsAccount("SA123", 1000)
current_account = CurrentAccount("CA456", 2000)

# Test deposit/withdraw
savings_account.deposit(500)    # Deposited: 500. New balance: 1500
savings_account.withdraw(200)   # Withdrew: 200. New balance: 1300
current_account.deposit(1000)   # Deposited: 1000. New balance: 3000
current_account.withdraw(500)   # Withdrew: 500. New balance: 2500

# Test getter/setter
print(f"Savings balance: {savings_account.get_balance()}")  # 1300
savings_account.set_balance(2000)
print(f"New savings balance: {savings_account.get_balance()}")  # 2000