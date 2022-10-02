# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def InputList(inputText):
    isNumber = False
    while not isNumber:
        try:
            numbers = [int(i) for i in input(f'{inputText}').split()]
            isNumber = True      
        except ValueError:
            print("Вы ввели не число или число не целое")
    return numbers 

def ProductsOfPairs(numericList):
    lengthOfList = 0
    products = []
    if len(numericList) % 2 == 0:
        lengthOfList = len(numericList) // 2
    else:
        lengthOfList = len(numericList) // 2 + 1
    for i in range(0, lengthOfList):
        products.append(numericList[i] * numericList[len(numericList) - i - 1])
    return products


numericList = InputList("Введите числа через пробел: ")
print(numericList)    

productsOfPairs = ProductsOfPairs(numericList)
print(productsOfPairs) 