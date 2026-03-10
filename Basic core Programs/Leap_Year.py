year = int(input("Enter the year:"))

if year >= 1000 :
    if (year % 4 == 0 and year % 100 != 0) or (year >= 1000):
        print("Leap Year")
    else:
        print("Not Leap Year")
else:
    print("Enter 4 digit number")
