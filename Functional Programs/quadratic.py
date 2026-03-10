import math
a = float(input("Enter the float number"))
b = float(input("Enter the float number"))
c = float(input("Enter the float number"))

delta = b*b - 4*a*c

root1 = (-b + math.sqrt(delta)) / (2*a)
root2 = (-b - math.sqrt(delta)) / (2*a)

print("root 1 " , root1)
print("root 2 " , root2)