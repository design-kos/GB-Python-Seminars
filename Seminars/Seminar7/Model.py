import re

def check_number(phone):
    pattern = r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"

    phone = phone.replace(" ", "")
    phone = phone.replace("-", "")
    phone = phone.replace("(", "")
    phone = phone.replace(")", "")
    phone = phone.replace("+7", "8")

    result = str(re.findall(pattern, phone))
    return result


def create_string(name, phone):
    text = name + " - " + phone
    return text