# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным

def InputNumbers(inputText):
    isNumber = False
    while not isNumber:
        try:
            number = int(input(f"{inputText}"))
            isNumber = True
        except ValueError:
            print("Вы ввели не число")
    return number


def CheckNumber(num):
    if 6 <= num <= 7:
        print(f"{num} день недели является выходным")
    elif 0 < num < 6:
        print(f"{num} день недели не является выходным")
    else:
        print(f"Число {num} выходит за пределы 7 дней")


num = InputNumbers("Введите номер дня недели: ")
CheckNumber(num)



