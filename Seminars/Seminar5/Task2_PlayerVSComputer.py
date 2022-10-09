# Создайте программу для игры в "Крестики-нолики". 

def PrintBoard():
    print(board[0], end = " ")
    print(board[1], end = " ")
    print(board[2])
 
    print(board[3], end = " ")
    print(board[4], end = " ")
    print(board[5])
 
    print(board[6], end = " ")
    print(board[7], end = " ")
    print(board[8])
     
def MakeMove(move,symbol):
    i = board.index(move)
    board[i] = symbol
 
def GetWinner():
    win = ""
    for i in victories:
        if board[i[0]] == "X" and board[i[1]] == "X" and board[i[2]] == "X":
            win = "X"
        if board[i[0]] == "O" and board[i[1]] == "O" and board[i[2]] == "O":
            win = "O"              
    return win
 
def CheckVictories(sum_O,sum_X):
    move = ""
    for line in victories:
        o = 0
        x = 0
        for j in range(0,3):
            if board[line[j]] == "O":
                o = o + 1
            if board[line[j]] == "X":
                x = x + 1
        if o == sum_O and x == sum_X:
            for j in range(0,3):
                if board[line[j]] != "O" and board[line[j]] != "X":
                    move = board[line[j]]
    return move
 
def AI():        
    move = ""
    move = CheckVictories(2,0)
    if move == "":
        move = CheckVictories(0,2)        
    if move == "":
        move = CheckVictories(1,0)           
    if move == "":
        if board[4] != "X" and board[4] != "O":
            move = 5           
    if move == "":
        if board[0] != "X" and board[0] != "O":
            move = 1           
    return move


# Основная программа  

board = [1,2,3,
        4,5,6,
        7,8,9]

start = board[0]
finish = board[-1]

victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]

gameOver = False
human = True
 
while gameOver == False:
    PrintBoard()
    if human == True:
        symbol = "X"
        isNumber = False
        while not isNumber:
            try:
                move = int(input("Человек, ваш ход: "))
                if (move >= start and move <= finish and move == board[move-1]):
                    isNumber = True
                    break
                else:
                    print("Вы указали число за переделами доски или поле уже занято")  
            except:
                print("Вы ввели не число или число не целое") 
    else:
        print("Компьютер делает ход: ")
        symbol = "O"
        move = AI()
    if move != "":
        MakeMove(move,symbol)
        win = GetWinner()
        if win != "":
            gameOver = True
        else:
            gameOver = False
    else:
        print("Ничья!")
        gameOver = True
        win = "дружба"
    human = not(human)        
 
PrintBoard()
print("Победил", win)   