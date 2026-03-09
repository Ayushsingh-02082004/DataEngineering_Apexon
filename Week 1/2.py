import random
num = int(input("Enter a number: "))
heads = 0 
tails = 0

for i in range(num):
    flip = random.random() #generates number between o and 1
    
    if flip < 0.5:
        tails += 1
    else:
        heads +=1

# Calcuate Percentage

head_percentage = (heads/num)* 100
tail_percentage = (tails/num)* 100

print("Heads precentage:" , head_percentage)
print("Tails percentage:" , tail_percentage)



