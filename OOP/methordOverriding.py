class BankAccount:
    def get_intrestRate(self):
        return 4.0
    
class SavingsAccount(BankAccount):
    def get_intrestRate(self):
        return 6.0
    
class FDAccount(BankAccount):
    def get_intrestRate(self):
        return 8.0
    

accounts = [BankAccount() , SavingsAccount() , FDAccount()]

for acc in accounts:
    print(f"Intrest rate is {acc.get_intrestRate()} percent.")

# in python there is not any concept of methord overloading as it simply overWrites the previous one .

class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c): # This OVERWRITES the previous 'add'
        return a + b + c

calc = Calculator()
# print(calc.add(1, 2))  <-- This would throw a TypeError! 
# It expects 3 arguments now because the 2-argument version is GONE.