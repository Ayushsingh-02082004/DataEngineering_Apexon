#Armstrong number is sum of cube of its digit 

num = int(input("Enter the number : "))

temp = num
sum = 0

while temp > 0: 
    digit = temp % 10
    sum += digit ** 3
    temp = temp // 10

if sum == num:
    print("YES")
else:
    print("No")