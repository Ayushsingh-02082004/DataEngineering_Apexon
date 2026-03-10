distance = int(input("Enter the distance : "))
age = int(input("Enter the age : "))

discount = 0

if age >= 60:
    discount += 0.30
if age <= 12:
    discount += 0.50


fare = distance*2 
finalfare = fare - (fare * discount)

print(finalfare)