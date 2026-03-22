from abc import ABC, abstractmethod

class IncomeTax(ABC):

    @abstractmethod
    def paytax(self, income):
        pass

    @abstractmethod
    def incometaxreturn(self, income, expense, tax):
        pass

    @abstractmethod
    def refund(self, redemption, tax):
        pass

# --- Concrete Implementation ---

class IndividualTax(IncomeTax):
    
    def paytax(self, income):
        tax = 0
        if income >= 1500000:
            tax = income * 0.18
        elif 1000000 <= income < 1500000:
            tax = income * 0.12
        elif 500000 <= income < 1000000:
            tax = income * 0.05
        else:
            tax = 0
        return tax
    
    def incometaxreturn(self, income, expense, tax):
        redemption = 0
        # If expenses are very high (over 80% of income), no redemption (luxury check)
        if expense > income * 0.80:
            redemption = tax*.90
        # If expenses are moderate (50% to 80%), high redemption
        elif expense >= income * 0.50:
            redemption = tax * 0.70
        # Low expenses, low redemption
        else:
            redemption = tax * 0.30
        return redemption
    
    def refund(self, redemption, tax):
        # The refund is the portion of the tax that is 'redeemed' back to the user
        if redemption > 0:
            print(f"Tax Refund calculated successfully!")
            return redemption
        else:
            print("No refund applicable based on expenses.")
            return 0

# --- Execution ---
tax_payer = IndividualTax()
my_income = 1200000
my_expense = 700000

# 1. Calculate Tax
tax_paid = tax_payer.paytax(my_income)

# 2. Calculate Redemption (Return)
return_amt = tax_payer.incometaxreturn(my_income, my_expense, tax_paid)

# 3. Get the Refund
final_refund = tax_payer.refund(return_amt, tax_paid)

print(f"Income: {my_income} | Tax Paid: {tax_paid} | Refund Amount: {final_refund}")
