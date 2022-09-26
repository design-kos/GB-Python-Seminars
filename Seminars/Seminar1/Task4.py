# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def InputQuarter(finish):  
    start = 0
    while start < finish:
        try:
            numOfQuarter = int(input(f"Введите номер четверти координатной плоскости: "))  
            start += 1
        except ValueError:
            print("Вы ввели не число")  
    return numOfQuarter

def CheckQuarter(numOfQuarter):
    if numOfQuarter < 1 or numOfQuarter > 4:
        print(f"Плоскости с таким номером не существует") 
    elif numOfQuarter == 1:
        print(f'В четверти №{numOfQuarter} x > 0 и y > 0')
    elif numOfQuarter == 2:
        print(f'В четверти №{numOfQuarter} x < 0 и y > 0')
    elif numOfQuarter == 3:
        print(f'В четверти №{numOfQuarter} x < 0 и y < 0')
    elif numOfQuarter == 4:
        print(f'В четверти №{numOfQuarter} x > 0 и y < 0')

numOfQuarter = InputQuarter(1)
CheckQuarter(numOfQuarter)        