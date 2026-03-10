n = int(input("Enter the number : "))

original = n
reversed = 0

while n > 0:
    reversed = reversed*10 + n % 10
    n = n// 10

if reversed == original:
    print("yes it is palindrome number . ")
else:
    print("No it is no palindrom number : ")