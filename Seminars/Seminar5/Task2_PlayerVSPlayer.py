# Создайте программу для игры в "Крестики-нолики". 

from random import randint

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
            win = firstPlayer
        if board[i[0]] == "O" and board[i[1]] == "O" and board[i[2]] == "O":
            win = secondPlayer             
    return win


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

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
flag = randint(0,2)
if flag:
    firstPlayer = player1
    secondPlayer = player2
    print(f"Первым ходит {firstPlayer}")
else:
    firstPlayer = player2
    secondPlayer = player1
    flag = True
    print(f"Первым ходит {firstPlayer}")
 
while gameOver == False:
    PrintBoard()
    if flag:
        symbol = "X"
        isNumber = False
        while not isNumber:
            try:
                move = int(input(f"{firstPlayer}, ваш ход: "))
                if (move >= start and move <= finish and move == board[move-1]):
                    isNumber = True
                    break
                else:
                    print("Вы указали число за переделами доски или поле уже занято")  
            except:
                print("Вы ввели не число или число не целое") 
        flag = False
    else:
        symbol = "O"
        isNumber = False
        while not isNumber:
            try:
                move = int(input(f"{secondPlayer}, ваш ход: "))
                if (move >= start and move <= finish and move == board[move-1]):
                    isNumber = True
                    break
                else:
                    print("Вы указали число за переделами доски или поле уже занято")  
            except:
                print("Вы ввели не число или число не целое") 
        flag = True

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
 
PrintBoard()
print("Победил", win)   