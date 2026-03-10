import random

heads = 0
tails = 0

n = int(input("Enter the number:" ))

for i in range(n):
    flip = random.random()

    if flip < 0.5:
        tails += 1
    else:
        heads += 1

headPercentage = (heads/n)*100
tailPercentage = (tails/n)*100

print("Heads Percentage: " , headPercentage)
print("Tails Percentage : " , tailPercentage)


