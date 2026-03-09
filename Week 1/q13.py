#palindrome string 

str = input("Enter the string : ")

reversed = ""

for char in str:
    reversed = char + reversed

if str == reversed:
    print("Both the string are plaindrome string")
else:
    print("Strings are not palindrome string")