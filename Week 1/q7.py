#factorial of a number

n = int(input("Enter a number : "))
total = 1;

for i in range(n , 1 , -1 ):
    total *= i
    print(total)


print("total sum is : "  , total)