# diplays the tic-tac-toe board
def print_board(a):
    print(f"\t  {a[0]}   |  {a[1]}   |  {a[2]}  ")
    print(f"\t-----|-----|-----")
    print(f"\t  {a[3]}   |  {a[4]}   |  {a[5]}  ")
    print(f"\t-----|-----|-----")
    print(f"\t  {a[6]}   |  {a[7]}   |  {a[8]}  ")


# displays the instruction of the game
def print_instructions():
    print("\n--------WELCOME TO TIC TAC TOE----------\n\n")
    print_board(position)
    print()

    player[0] = input("Enter Player1 name : ")
    player[1] = input("Enter Player2 name : ")

    print("\n------Instructions-------")
    print(f"{player[0]} you will be using X")
    print(f"{player[1]} you will be using O")
    print(f"Turn starts from {player[0]}")
    print("Positions are like :")
    print("\t 1 | 2 | 3 ")
    print("\t---|---|---")
    print("\t 4 | 5 | 6 ")
    print("\t---|---|---")
    print("\t 7 | 8 | 9 ")
    print("Press S to start the game")
    start = input()
    return start

# function to start the game
def startgame():
    turn=0
    for i in range(9):
        if turn == 0:
            print(f"\n {player[0]}, it's your turn")
            p = int(input("Please Enter your position : "))
            v = 'X'
            position[p-1] =v
            print_board(position)
            winner = check_winner(v)
            if winner is "nobody":
                turn = 1
                continue
            else:
                print(f"\n Hurray!! '{player[0]}' you Win")
                break
        else:
            print(f"\n {player[1]}, it's your turn")
            p = int(input("Please Enter your position : "))
            v = 'O'
            position[p-1] = v
            print_board(position)
            winner = check_winner(v)
            if winner is "nobody":
                turn = 0
                continue
            else:
                print(f"\n Hurray!! '{player[1]}' you Win")
                break
    else:
        print("\n\n Game is Tie")

#checks for winner
def check_winner(v):
    for i in winning_conditions:
        if(position[i[0]],position[i[1]],position[i[2]]) == (v,v,v):
            winner = player[0]
            break
        elif (position[i[0]],position[i[1]],position[i[2]]) == (v,v,v):
            winner = player[1]
            break
    else:
        winner = "nobody"
    return winner




position = ['' for i in range(9)]
player = ['','']
winning_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
start = print_instructions()
if start == 's' or start == 'S':
    startgame()
else:
    print("Invalid Entry")