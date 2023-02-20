from dataclasses import dataclass


@dataclass
class Field_:
    field_data: str | int | bool = None


    def is_filled(self, context: str, data=None):
        data = input(f"{context}: ")
        if data == "":
            print("\033[1;31mДанные не заполнены!\033[0m\n")
            return self.is_filled(context)
        else:
            return data


    def get_type_field(self, context: str, data: str | None = None):
        type_dict = {
            "varchar": "строковый",
            "numeric": "числовой",
            "datetime": "дата, время",
            "date": "дата",
        }
        data = self.is_filled(context, data)
        if data not in type_dict:
            print("\033[1;31mДоступные типы данных\033[0m:",)
            for k, v in type_dict.items():
                print(f"\033[1;34m{k:15}\033[0m {v}")
            print()
            return self.get_type_field(context)
        else:
            return data


    def get_length_field(
            self, context: str, 
            data_type: str, 
            data: int | None = None):

        if data_type in ["datetime", "date"]:
            return None
        else:
            try:
                data = int(self.is_filled(context, data))
                return data
            except:
                print("\033[1;31mДоступен ввод только целого числа\033[0m:\n",)
                return self.get_length_field(context, data_type)

    
    def get_fsure_field(self, context: str, data=None):
        data = self.is_filled(context, data)
        if data == "0":
            return False
        elif data == "1":
            return True
        else:
            print("\033[1;31mДоступные ключи для ввода\033[0m:")
            print(f"\033[1;34m0\033[0m\tтег необязательный")
            print(f"\033[1;34m1\033[0m\tтег обязательный\n")
            return self.get_fsure_field(context)




@dataclass
class Tag:
    t_name: str
    t_type: str
    t_len: int | None
    t_sure: bool


@dataclass
class Header:
    e_name: str
    tags: list[Tag]