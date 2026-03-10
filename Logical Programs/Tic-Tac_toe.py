import random


board = [[" " for _ in range(3)] for _ in range(3)]  #it creates 3*3 grid filled with the spaces 

def printboard():
    for row in board:
        print("|".join(row))
        print("-"*5)


#check Winner

def check_winner(player):

    #check rows
    for row in board:
        if all (cell == player for cell in row):
            return true
        
    #check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
        
    #check Diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

#check if board full
def board_full():
    for row in board:
        if " " in row:
            return False
        
    return True

#Game loop

while True:

    print("\ncurrent Board: ")
    printboard()

    #user move

    row = int(input("Enter row 0-2 : "))
    col = int(input("Enter column 0-2 : "))


    if board[row][col] == " ":
        board[row][col] = "x"
    else: 
        print("Cell already taken.Try again.")
        continue

    #check user win
    if check_winner("x"):
        printboard()
        print("User wins------wins")
        break

    #check draw
    if board_full():
        printboard()
        print("Game Draw")
        break

    #computer move

    while True:
        r = random.randint(0,2)
        c = random.randint(0,2)

        if board[r][c] == " ":
            board[r][c] = "0"
            print("Computer move : ", r , c)
            break

    #check Computer win
    if check_winner("0"):
        printboard()
        print("Computer wins")
        break

    #check draw again
    if board_full():
        printboard()
        print("Game Draw")
        break

    