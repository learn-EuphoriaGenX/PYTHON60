class ReserveBankOfIndia:
    def __init__(self, name):
        self.name = name # Public attribute
        self.__gold_reserve = 1000  # Private attribute

    # Public method to access private attribute
    # setter method
    def set_gold_reserve(self, amount):
        if amount >= 0:
            self.__gold_reserve += amount
        else:
            print("Gold reserve cannot be negative.")
    # getter method
    def get_gold_reserve(self):
        return self.__gold_reserve

# rb1 = ReserveBankOfIndia("RBI")
# print(rb1.name)  # Accessing public attribute
# # print(rb1.__gold_reserve)  # This will raise an AttributeError
# rb1.set_gold_reserve(500)  # Adding gold to the reserve
# print(rb1.get_gold_reserve())  # Accessing private attribute through getter method

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.__balance
    
class SBI(BankAccount):
    def show_balance(self):
        print(f"Account Holder: {self.account_holder}, Balance: {self.get_balance()}")
   
    

# account = BankAccount("Alice", 1000)
# account.deposit(500)
# account.withdraw(200)
# print(f"Current balance: {account.get_balance()}")
sbi_account = SBI("Bob", 1500)
sbi_account.show_balance()

