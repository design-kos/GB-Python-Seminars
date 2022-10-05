# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random
import pathlib
from pathlib import Path
import os

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

def RandomNumbers():
    return random.randint(0,101)

def CreatingCoefficients(k):
    coefficients = [RandomNumbers() for i in range(k+1)]
    return coefficients    

def CreatingString(value):
    lst = value[::-1]
    characters = ''
    if len(lst) < 1:
        characters = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                characters += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    characters += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                characters += f'{lst[i]}x'
                if lst[i+1] != 0:
                    characters += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                characters += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                characters += ' = 0'
    return characters

def CreatingFile(polynomial):
    path = Path(pathlib.Path.cwd(), 'Seminars', 'Seminar4', 'polynomial.txt')
    filepath = os.path.join(path)
    with open(filepath, "w") as data:
        data.write(polynomial) 

k = InputNumber("Введите целое натуральное число: ") 
coefficients = CreatingCoefficients(k)
CreatingFile(CreatingString(coefficients))