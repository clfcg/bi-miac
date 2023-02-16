TYPES_DICT = {
    "text": "varchar",
    "num": "numeric",
    "date": "date",
    "datetime": "datetime"
}

def check_type(type_name: str):
    if type_name not in TYPES_DICT:
        print("Доступные типы данных", [t for t in TYPES_DICT.keys()])
        return False
    else:
        return True


check_type("numeric")