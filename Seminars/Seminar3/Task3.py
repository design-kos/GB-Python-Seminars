# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.

def InputList(inputText):
    isNumber = False
    while not isNumber:
        try:
            numbers = [float(i) for i in input(f'{inputText}').split()]
            isNumber = True      
        except ValueError:
            print("Вы ввели не число")
    return numbers 

def RemoveDigitsBeforeDecimalPoint(numericList):
    result = []
    for i in numericList:
        if i % 1 != 0:
            result.append(round(i % 1, 2))
    return result

def FindDifferenceBetweenMaxAndMin(numericList):
    result = max(numericList) - min(numericList)
    return result

numericList = InputList("Введите вещественные числа через пробел: ")
print(numericList)      

numericListWithoutIntegerPart = RemoveDigitsBeforeDecimalPoint(numericList)
print(numericListWithoutIntegerPart)

DifferenceBetweenMaxAndMin = FindDifferenceBetweenMaxAndMin(numericListWithoutIntegerPart)
print(DifferenceBetweenMaxAndMin)