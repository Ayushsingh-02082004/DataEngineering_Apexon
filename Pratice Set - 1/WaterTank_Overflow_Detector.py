n = int(input("Enter the nimutes : "))

inflows = list(map(int , input("Enter the inflows : ").split()))

capacity = 1000
volume = 0
overflow = False

for  i in range(len(inflows)):
    volume += inflows[i]
    n -= 1

    if volume > capacity:
        print(i+1)
        overflow = True
        break


if not overflow:
    print("no overflow")