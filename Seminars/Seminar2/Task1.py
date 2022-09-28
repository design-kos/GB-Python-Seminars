# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def InputNumber(inputText):
    isNumber = False
    while not isNumber:
        try:
            number = float(input(f"{inputText}"))
            isNumber = True
        except ValueError:
            print("Вы ввели не число")
    return number

def SumOfDigits(number):
    sum = 0
    for i in str(number):
        if i != ".":
            sum += int(i)
    return sum

number = InputNumber("Введите число: ")
sum = SumOfDigits(number)
print(f"Сумма цифр числа {number} равна {sum}")