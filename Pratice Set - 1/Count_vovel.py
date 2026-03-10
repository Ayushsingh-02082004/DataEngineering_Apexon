str = input("Enter the string to count vovel")

count = 0

for char in str:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        count += 1

print(str , "Contains " , count , "Vovels")