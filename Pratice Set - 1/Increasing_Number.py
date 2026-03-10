num = input("Enter the number : ")

increasing = True

for i in range(len(num) -1 ):
    if num[i] >= num[i+1]:
        increasing = False
        break

if increasing:
    print("YES")
else:
    print("NO")