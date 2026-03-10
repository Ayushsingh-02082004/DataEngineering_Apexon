balance = int(input("Enter the balance amount : "))
n = int(input("Enter the number of transactions : "))


for i in range(n):
    amount = int(input("Enter the amount you want to withdraw : "))

    if amount % 100 == 0 and balance >= amount:
        balance -= amount
        print("Success")

    else:
        print("Failed")

print(balance)