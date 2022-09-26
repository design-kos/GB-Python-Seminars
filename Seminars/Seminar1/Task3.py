# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

def InputCoordinates(finish):
    xy = ["X", "Y"]
    a = [0] * finish
    start = 0
    while start < finish:
        try:
            for i in range(start, finish): 
                number = int(input(f"Введите координату {xy[i]}: "))
                a[i] = number
                checkZero = 1 / a[i]
                if i >= finish - 1:
                    start = finish  
        except ZeroDivisionError:
            print("Координата не должно быть равна 0 ")   
            start = i                   
        except ValueError:
            print("Вы ввели не число")  
            start = i
    return a


def CheckCoordinates(xy):
    if xy[0] > 0 and xy[1] > 0:
        print(f"Точка находится в 1-й четверти плоскости") 
    elif xy[0] < 0 and xy[1] > 0:
        print(f"Точка находится во 2-й четверти плоскости") 
    elif xy[0] < 0 and xy[1] < 0:
        print(f"Точка находится в 3-й четверти плоскости") 
    elif xy[0] > 0 and xy[1] < 0:
        print(f"Точка находится в 4-й четверти плоскости") 


coordinates = InputCoordinates(2)
CheckCoordinates(coordinates)