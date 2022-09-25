# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def inputNumbers(finish):
    xyz = ["X", "Y", "Z"]
    a = []
    start = 0
    while start < finish:
        try:
            for i in range(start, finish): 
                a.append(int(input(f"Введите значение {xyz[i]}: "))) 
                if i >= finish - 1:
                    start = finish     
        except ValueError:
            print("Вы ввели не число")  
            start = i
    return a


def checkPredicate(x):
    leftValue = not (x[0] or x[1] or x[2])
    rightValue = not x[0] and not x[1] and not x[2]
    result = leftValue == rightValue
    return result


statement = inputNumbers(3)

if checkPredicate(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")