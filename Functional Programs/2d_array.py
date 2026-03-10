m = int(input("Enter number of rows : "))
n = int(input("Enter number of cols : "))

arr = []

print("Enter the elements: ")


for i in range(m):
    row = []
    for j in range(n):
        value = int(input())
        row.append(value)
    arr.append(row)

print("2D Array is : ")

for i in range(m):
    for j in range(n):
        print(arr[i][j] , end = " ")
    print()