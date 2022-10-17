import Logger
import Model

def input_name():
    name = input("Введите ФИО контакта: ")
    return name

def input_phone():
    phone = input("Укажите один или несколько номеров телефона через запятую: ")
    return phone

name = input_name()
phone = Model.check_number(input_phone())
Logger.write_contact(Model.create_string(name, phone))