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

def SumOfNumbersWithOddIndexes(numericList):
    count = 0
    for i in range(len(numericList)):
        if i % 2 == 0:
            count += numericList[i]
    return count

numericList = InputList("Введите числа через пробел: ")
print(numericList)

sumOfNumbers = SumOfNumbersWithOddIndexes(numericList)
print(sumOfNumbers)