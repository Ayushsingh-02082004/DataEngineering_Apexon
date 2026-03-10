import random


stake = int(input("Enter stake : "))
goal = int(input("Enter goal : "))
trials = int(input("Enter number of experiments : "))


wins = 0
bets = 0


for i in range(trials):

    cash = stake
    while cash > 0 and cash < goal :

        bets += 1
        if random.random() < 0.5:
            cash += 1
        else:
            cash -= 1;

    if cash == goal:
        wins += 1

win_percent = (wins / trials) * 100
loss_percent = 100 - win_percent


print("Number of wins =" , wins)
print("win percentage = " , win_percent)
print("Loss Percentage ", loss_percent)