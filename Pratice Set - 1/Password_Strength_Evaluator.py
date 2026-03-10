password = input("Enter the password : ")

digit = False
uppercase = False
length = False

if len(password) >= 8:
    length = True


for char in password : 
    if char.isdigit() : 
        digit = True
    elif char.isupper() : 
        uppercase = True

if digit == True and uppercase == True and length == True:
    print("STRONG")
else :
    print("Weak password")
    