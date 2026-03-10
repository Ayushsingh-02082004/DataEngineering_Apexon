units = int(input("Enter the units of electricity used : "))


bill = 0

#first 100 unit 

if units <= 100:
    bill = units * 3

#first 200 units

elif units <= 200:
    bill = units * 5

#Above 200 units
else:
    bill = (100 * 3) + (100 * 5) + (units - 200)*8

#surcharge if bill > 300

if units > 300:
    bill = bill + (bill * 0.10)

print("Total bill:" , int(bill))

