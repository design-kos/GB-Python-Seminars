# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

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

def Progression(n):
    result = []
    count = 1
    for i in range(1, n+1):
        count = (1 + 1 / i) ** i
        result.append(count)
    return result

def SumOfNumbersFromProgression(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum

number = InputNumber("Введите целое число больше нуля: ")
prog = Progression(number)
sum = SumOfNumbersFromProgression(prog)
print(f"Последовательность(1+1/n)^n для чисел 1 до {number} - {prog}")
print(f"Сумма чисел последовательности равна {sum}")