# Напишите программу, которая будет преобразовывать десятичное число в двоичное

def InputNumbers(inputText):
    isNumber = False
    while not isNumber:
        try:
            number = int(input(f"{inputText}"))
            isNumber = True
        except ValueError:
            print("Вы ввели не число или число не целое")
    return number

def ConvertingNumberToBinary(number):
    numberBinary = ''
    while number > 0:
        numberBinary = str(number % 2) + numberBinary
        number = number // 2
    return numberBinary

num = InputNumbers("Введите целое число: ")
numBinary = ConvertingNumberToBinary(num)
print(f"Число {num} в двоичной системе исчесления - {numBinary}")