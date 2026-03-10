num = int(input("Enter the number : "))

while num >= 10:
    digitsum = 0

    while num > 0:
        digitsum += num % 10
        num = num//10

    num  = digitsum

print(num)