correctPin = input("Enter the correct PIN: ")

access = False

for i in range(3):
    attempt == input("Enter PIN: ")

    if attempt == correctPin :
       access = True
       break

if access:
    print("Access Granted : ")
else : 
    print("Locked ")