# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

from math import factorial

def InputNumber(inputText):
    isNumber = False
    start = 1
    while not isNumber:
        try:
            number = int(input(f"{inputText}"))
            if number >= start:
                isNumber = True
                break
            else:
                print("Вы ввели не натуральное число")  
        except ValueError:
            print("Вы ввели не число или число не целое")  
    return number

n = InputNumber("Введите целое натуральное число: ")
f = lambda x: 1 if x == 0 else x * factorial(x - 1)
numericList = list( f(i) for i in range(1, n +1))
print(numericList)