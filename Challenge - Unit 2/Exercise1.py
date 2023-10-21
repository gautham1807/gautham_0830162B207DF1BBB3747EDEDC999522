class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Rs.{amount} deposited successfully.\nNew balance is Rs.{self.__account_balance:.2f}"
        else:
            return "Invalid deposit amount. Please enter a positive amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Rs.{amount} withdrawn successfully.\nNew balance is Rs.{self.__account_balance:.2f}"
        elif amount <= 0:
            return "Invalid withdrawal amount. Please enter a positive amount."
        else:
            return "Insufficient funds for withdrawal."

    def display_balance(self):
        return f"Account Number : {self.__account_number}\nAccount Holder Name : {self.__account_holder_name}\nAccount Balance : Rs.{self.__account_balance:.2f}"


account = BankAccount(123 , "Gautham",1000.00)
print(account.display_balance())  
print(account.deposit(500)) 
print(account.withdraw(200)) 
  

