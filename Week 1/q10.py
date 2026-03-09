# factors of the number 

n = int(input("Enter the number to know its factors"))

for i in range(1 , n ):
    if(n % i == 0):
        print(i , " is a factor of " , n)
        