amount = int(input("Enter the amount : "))

discount = 0

if amount >= 5000:
    discount += 0.20
elif amount >= 3000:
    discount += 0.10
elif amount >= 1000:
    discount += 0.05

finalamount = amount - (amount*discount)

print("Final Amount is : " , finalamount)
