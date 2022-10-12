# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def InputList(inputText):
    isNumber = False
    while not isNumber:
        try:
            numbers = [int(i) for i in input(f'{inputText}').split()]
            isNumber = True      
        except ValueError:
            print("Вы ввели не число или число не целое")
    return numbers 

print(sum(x for i, x in enumerate(InputList("Введите числа через пробел: ")) if i % 2 != 0))