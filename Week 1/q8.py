#print the sum of all even and odd numbers in a range

n = int(input("Enter the numer to find even odd sum"))

eventotal = 0
oddtotal = 0

for i in range(1 , n+1 , 1):
    if( i % 2 == 0):
        eventotal += i
    else:
        oddtotal += i


print("Even sum is : " , eventotal)
print("Odd sum is " , oddtotal)