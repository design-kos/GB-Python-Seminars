# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

from cmath import sqrt


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

a = InputNumber("Введите первое целое натуральное число: ")
b = InputNumber("Введите второе целое натуральное число: ")
print(f"Является ли одно из введенных чисел квадратом другого: {sqrt(a) == b or sqrt(b) == a}")