import random

n = int(input("ENter the number :"))


def generateRandom(n):
    return random.randint(1 , n)


def distince_coupons(n):
    collected = set()
    count = 0

    while len(collected) < n:
        num = generateRandom(n)
        count += 1

        if num not in collected:
            collected.add(num)

    return count

result = distince_coupons(n)

print("Count is ", result)