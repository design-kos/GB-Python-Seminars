# Вычислить число c заданной точностью d

from math import pi

def InputNumber(inputText):
    isNumber = False
    start = pow(10, -1)
    finish = pow(10, -10)
    while not isNumber:
        try:
            number = float(input(f"{inputText}"))
            if (number <= start and number >= finish):
                isNumber = True
                break
            else:
                print("Вы ввели число вне диапазона от 0.1 до 0.0000000001")  
        except ValueError:
            print("Вы ввели не число")  
    return number

d = InputNumber("Введите число от 0.1 до 0.0000000001: ")    
print(f"Число Пи с точностью {d} равно {round(pi, len(str(d)) - 2)}")