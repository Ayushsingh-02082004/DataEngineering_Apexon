import math

a = int(input("Enter the start range : "))
b = int(input("Enter the end range : "))

count = 0

for n in range (a , b+1):
    if n > 1:
        is_prime = True
        for i in range(2 , int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1


print(count)