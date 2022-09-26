# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

def InputNumbers(finish):
    xy = ["X", "Y"]
    a = []
    start = 0
    while start < finish:
        try:
            for i in range(start, finish): 
                a.append(int(input(f"Координата по оси {xy[i]}: "))) 
                if i >= finish - 1:
                    start = finish     
        except ValueError:
            print("Вы ввели не число")  
            start = i
    return a

def FindDistanceBetweenPoints(a, b):
    distance = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return distance

print("Введите координаты точки А")
a = InputNumbers(2)
print("Введите координаты точки В")
b = InputNumbers(2)
print (b)

distance = FindDistanceBetweenPoints(a, b)
print(f"Расстояние между точкой A{a} и точкой B{b} равно {format(distance, '.2f')}")