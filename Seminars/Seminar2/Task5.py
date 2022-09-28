# Реализуйте алгоритм перемешивания списка.

import random

def InputNumber(inputText):
    isNumber = False
    while not isNumber:
        try:
            number = int(input(f"{inputText}"))
            checkZero = 1 / number
            isNumber = True
        except ZeroDivisionError:
            print("Число не должно быть равно 0 ")        
        except ValueError:
            print("Вы ввели не число или число не целое")
    return number

def ListGeneration(n):
    result = []
    for i in range(-n, n+1):
        result.append(i)
    return result     

number = InputNumber("Введите целое число больше нуля: ")
list = ListGeneration(number)
print(f"Последовательность чисел от -{number} до {number} - {list}")

random.shuffle(list)
print(f"Перемешанный список чисел от -{number} до {number} - {list}")
