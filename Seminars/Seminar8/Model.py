from inspect import Attribute

attributes = ["ID", "Имя", "Телефон", "Должность", "Зарплата"]

def input_info():
    id = input("Введите ID сотрудника: ")
    name = input("Введите ФИО сотрудника: ")
    phone = input("Введите номер телефона сотрудника: ")
    post = input("Введите должность сотрудника: ")
    wage = input("Введите зарплату сотрудника: ")
    return f'{id}, {name}, {phone}, {post}, {wage}\n'

def input_request():
    return input("Введите данные для поиска: ")

def input_id():
    return int(input("Введите ID сотрудника: "))

def search_info(file, info, id):
    a = ""
    for i in file:
        for j in i:
            if j.find(info) != -1 and int(j[0]) == id:
                a = j
    if a == "":
        return("not found")
    else:
        return a

def choose_mode():
    return int(input("Добавление сотрудника - 1; Поиск сотрудника - 2, Замена информации о сотруднике - 3: "))

def change_info(file, id):
    print("Выберите, какую информацию о сотруднике вы хотите изменить: ")
    for i in range(len(attributes)):
        print(f"{i} - {attributes[i]}")
    mode = int(input())
    a = ""
    for k in file:
        for j in k:
            if int(j[0]) == id:
                a = j
    if a == "":
        print("id not found")
    elif a != "":
        new_line = a.split(", ")
        if mode <= len(attributes):
            change = input("Введите новую информацию: ")
            new_line[mode] = change
        else:
            print("Такого аттрибута не существует")
    new_info = ', '.join(new_line)
    return [a, new_info]

