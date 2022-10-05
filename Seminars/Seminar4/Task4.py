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

def GetPower(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num   

def GetCoefficient(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num  

def GetAllCoefficients(polynomial):
    polynomial = polynomial[0].replace(' ', '').split('=')
    polynomial = polynomial[0].split('+')
    lst = []
    l = len(polynomial)
    k = 0
    if GetPower(polynomial[-1]) == -1:
        lst.append(int(polynomial[-1]))
        l -= 1
        k = 1
    i = 1
    ii = l-1
    while ii >= 0:
        if GetPower(polynomial[ii]) != -1 and GetPower(polynomial[ii]) == i:
            lst.append(GetCoefficient(polynomial[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1
    return lst  

def SumOfTwoPolynomials(polynomial1, polynomial2):
    lst1 = GetAllCoefficients(polynomial1)
    lst2 = GetAllCoefficients(polynomial2)
    l1 = len(lst1)
    if len(lst1) > len(lst2):
        l1 = len(lst2)
    newLst = [lst1[i] + lst2[i] for i in range(l1)]
    if len(lst1) > len(lst2):
        l2 = len(lst1)
        for i in range(l1,l2):
            newLst.append(lst1[i])
    else:
        l2 = len(lst2)
        for i in range(l1,l2):
            newLst.append(lst2[i])
    return newLst

def CreatingFile(polynomial):
    path = Path(pathlib.Path.cwd(), 'Seminars', 'Seminar4', 'sumOfPolynomials(Task4).txt')
    filepath = os.path.join(path)
    with open(filepath, "w") as data:
        data.write(polynomial) 

# Создание и вывод первого многочлена
k1 = InputNumber("Введите целое натуральное число (степень для первого файла): ") 
coefficients1 = CreatingCoefficients(k1)
polynomial1 = CreatingString(coefficients1)
path1 = Path(pathlib.Path.cwd(), 'Seminars', 'Seminar4', 'polynomial1(Task4).txt')
filepath1 = os.path.join(path1)
with open(filepath1, "w") as data:
    data.write(polynomial1) 
with open(filepath1, 'r') as data:
    polynomial1String = data.readlines()    
print(f"Первый многочлен {polynomial1String}")    

# Создание и вывод второго многочлена
k2 = InputNumber("Введите целое натуральное число (степень для первого файла): ") 
coefficients2 = CreatingCoefficients(k2)
polynomial2 = CreatingString(coefficients2)
path2 = Path(pathlib.Path.cwd(), 'Seminars', 'Seminar4', 'polynomial2(Task4).txt')
filepath2 = os.path.join(path2)
with open(filepath2, "w") as data:
    data.write(polynomial2) 
with open(filepath2, 'r') as data:
    polynomial2String = data.readlines()   
print(f"Второй многочлен {polynomial2String}")  

# Создание и вывод результирующего многочлена
CreatingFile(CreatingString(SumOfTwoPolynomials(polynomial1String, polynomial2String)))
path = Path(pathlib.Path.cwd(), 'Seminars', 'Seminar4', 'sumOfPolynomials(Task4).txt')
filepath = os.path.join(path)
with open(filepath, 'r') as data:
    polynomialString = data.readlines()   
print(f"Сумма многочленов - {polynomialString}")