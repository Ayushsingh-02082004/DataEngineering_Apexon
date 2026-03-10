num = int(input("Enter the number : "))

count =0

while num % 2 == 0:
    num = num/2
    count += 1

print(count)