#code of perfect number 28  = 1 + 2 + 4 + 7 + 14 and all these are its divisors also

n = int(input("Enter the number : "))
sum = 0

for i in range(1 , n ):
    if( n % i  == 0):
        sum += i

if(sum == n):
    print(sum , " Is a perfect number.")
else:
    print(sum , " is not a perfect number")
