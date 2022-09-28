# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

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

def Multiplication(n):
    result = []
    count = 1
    for i in range(1, n+1):
        count = count * i
        result.append(count)
    return result

number = InputNumber("Введите целое число больше нуля: ")
multOfNumbers = Multiplication(number)
print(f"Набор произведений числе от 1 до {number} равно {multOfNumbers}")