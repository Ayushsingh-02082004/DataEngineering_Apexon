class BankAccount:
    
    def __init__(self , balance):
        self.__balance = balance  #private variable

    def deposit(self , amount):
        self.__balance += amount
        print("Deposited:" , amount)

    def withdraw(self , amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:" , amount)
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Current Balance:" , self.__balance)


# Creating object
account = BankAccount(1000)

account.deposit(500)
account.withdraw(200)
account.show_balance()