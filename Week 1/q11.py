#prime number

n = int(input("Enter the number to ckeck prime or not "))

for i in range(2, n ):
    if(n % i == 0):
        print(n ," is not prime number as it is divisible by ", i )
        break;
else:
    print("it is a prime number")