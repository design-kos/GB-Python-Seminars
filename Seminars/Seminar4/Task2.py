# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def InputNumber(inputText):
    isNumber = False
    start = 1
    while not isNumber:
        try:
            number = int(input(f"{inputText}"))
            if number >= start:
                isNumber = True
                break
            else:
                print("Вы ввели не натуральное число")  
        except ValueError:
            print("Вы ввели не число или число не целое")  
    return number

def Factors(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
           factors.append(i)
           n = n / i
        i += 1
    if n > 1:
        factors.append(int(n))
    elif n == 1:
        factors.append(int(n))
    return factors

n = InputNumber("Введите целое натуральное число: ") 
factors = Factors(n)
print(factors)