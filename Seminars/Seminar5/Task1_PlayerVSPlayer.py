# Задача №38: Создайте программу для игры с конфетами человек против человека. 
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# a) Добавьте игру против бота

# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Ответ: Первому игроку нужно каждый ход добирать относительно хода второго игрока 
# до максимально доступного количества конфет за 1 ход плюс 1. То есть, если второго игрок взял 8 конфет, 
# первому нужно взять 28 - 8 + 1. При этом первый ход первого игрока должен быть 2021 % (28 + 1) = 20

from random import randint

def InputNumber(name):
    isNumber = False
    start = 1
    finish = 28
    while not isNumber:
        try:
            number = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
            if (number >= start and number <= finish):
                isNumber = True
                break
            else:
                print("За один ход можно взять от 1 до 28 конфет!")  
        except ValueError:
            print("Вы ввели не число или число не целое")  
    return number

def ScorePrint(name, k, count, value):
    print(f"Ходил игрок {name}, он взял {k} конфет, теперь у него {count} конфет. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = 2021
flag = randint(0,2)
if flag:
    print(f"Первым ходит {player1}")
else:
    print(f"Первым ходит {player2}")

count1 = 0 
count2 = 0

while value > 28:
    if flag:
        k = InputNumber(player1)
        count1 += k
        value -= k
        flag = False
        ScorePrint(player1, k, count1, value)
    else:
        k = InputNumber(player2)
        count2 += k
        value -= k
        flag = True
        ScorePrint(player2, k, count2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")