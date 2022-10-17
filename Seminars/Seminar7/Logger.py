import pathlib
import os

def write_contact(contact):
    path = pathlib.Path(pathlib.Path.cwd(), 'Seminars', 'Seminar7', 'Phonebook.txt')
    filepath = os.path.join(path)
    with open(filepath, "a", encoding="utf-8") as data:
        data.write(f'{contact}\n')