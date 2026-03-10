n = int(input("Enter the number of requests: "))

seats = 40

for i in range(n):
    request = int(input("Enter required seats : "))

    if request <= seats:
        print("CONFIRMED")
        seats -= request
    else:
        print("WAITLISTED")