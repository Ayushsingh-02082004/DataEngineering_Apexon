import math

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

distance = math.sqrt(math.pow(x , 2) + math.pow(y,2))

print("Euclidean distance = " , distance)