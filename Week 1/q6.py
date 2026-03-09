#sum up to n terms

n = int(input("Enter the number to sum :"))
total = 0

for i in range(1 , n+1):
    total += i
    print(total)



print("sum = " , total)