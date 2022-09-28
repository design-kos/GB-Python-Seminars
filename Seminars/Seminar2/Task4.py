# Задайте список из 2N+1 элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

def InputNumber(inputText):
    isNumber = False
    while not isNumber:
        try:
            number = int(input(f"{inputText}"))
            checkZero = 1 / number
            isNumber = True
        except ZeroDivisionError:
            print("Число не должно быть равно 0 ")        
        except ValueError:
            print("Вы ввели не число или число не целое")
    return number

def ListGeneration(n):
    result = []
    for i in range(-n, n+1):
        result.append(i)
    return result

def InputIndexes(inputText):
    isNumber = False
    while not isNumber:
        try:
            selectedIndexes = [int(i) for i in input(f'{inputText}').split()]
            isNumber = True      
        except ValueError:
            print("Вы ввели не число или число не целое")
    return selectedIndexes 

def MultiplySelectedElements(list, indexes):
    product = 1
    for i in indexes:
        try:
            product = product * list[i]
        except IndexError:
            print(f"Индекс {i} выходит за пределы списка, поэтому он не будет учтен")
    return product       

number = InputNumber("Введите целое число больше нуля: ")
list = ListGeneration(number)
print(f"Последовательность чисел от -{number} до {number} - {list}")

indexes = InputIndexes("Введите индексы элементов из списка через пробел: ")
productOfSelectedElements = MultiplySelectedElements(list, indexes)
print(f"Произведение выбранных элементов равно {productOfSelectedElements}")
