def write_info(info, filepath):
    with open(filepath, "a", encoding="utf-8") as data:
        data.write(f'{info}')

def print_info(filepath):
    with open(filepath, "r", encoding="utf-8") as data:
        return data.read()   

def open_info(filepath):
    with open(filepath, "r", encoding="utf-8") as data:
        data = data.read().splitlines()
        a = []
        for line in data:
            line = line.split("\n")
            a.append(line)
        return a          

def replace_info(a, new_info, filepath):
    with open(filepath, 'r', encoding="utf-8") as data_original:
        x = data_original.read()
    with open(filepath, "wt", encoding="utf-8") as data_changed:
        x = x.replace(a, new_info)
        data_changed.write(x)