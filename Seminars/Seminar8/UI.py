import Logger
import Model
import pathlib
import os

path = pathlib.Path(pathlib.Path.cwd(), 'Seminars', 'Seminar8', 'Employees.txt')
filepath = os.path.join(path)

print(Logger.print_info(filepath))

while True:
    mode = Model.choose_mode()
    if mode == 1:
        Logger.write_info(Model.input_info(), filepath)
    elif mode == 2:
        info = Model.input_request()
        id = Model.input_id()
        file = Logger.open_info(filepath)
        print(Model.search_info(file, info, id))
    elif mode == 3:
        id = Model.input_id()
        file = Logger.open_info(filepath)
        change = (Model.change_info(file, id))
        print((str(change[0])))
        print((str(change[1])))
        Logger.replace_info(str(change[0]), str(change[1]), filepath)
    elif mode == 0:
        print("Выход")
        break
    else:
        print("Такого режима не сущестует")