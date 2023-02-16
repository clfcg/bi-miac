TYPES_DICT = {
    "text": "varchar",
    "num": "numeric",
    "date": "date",
    "datetime": "datetime",
}


def check_type(type_name: str):
    if type_name not in TYPES_DICT:
        print("Доступные типы данных", [t for t in TYPES_DICT.keys()])
        return False
    else:
        return True
    

def set_len(type_name: str):
    if type_name in ["text", "num"]:
        return True
    else:
        return None
    
#fix this
def check_data_filled(data):
    while data == "":
        print("Данные не введены!")
        check_data_filled(data)
    return data