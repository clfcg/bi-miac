from dataclasses import dataclass

from strictyaml import as_document


@dataclass
class Field_:
    field_data: str | int | bool = None

    def is_filled(self, context: str, data=None):
        data = input(f"{context}: ")
        if data == "":
            print("\033[1;31mДанные не заполнены!\033[0m\n")
            return self.is_filled(context)
        else:
            self.field_data = data
            return self.field_data

    def get_type_field(self, context: str, data: str | None = None):
        type_dict = {
            "varchar": "строковый",
            "numeric": "числовой",
            "datetime": "дата, время",
            "date": "дата",
        }
        data = self.is_filled(context, data)
        if data not in type_dict:
            print("\033[1;31mДоступные типы данных\033[0m:")
            for k, v in type_dict.items():
                print(f"\033[1;34m{k:15}\033[0m {v}")
            print()
            return self.get_type_field(context)
        else:
            self.field_data = data
            return self.field_data

    def get_length_field(
            self, context: str, 
            data_type: str, 
            data: int | None = None):

        if data_type in ["datetime", "date"]:
            return ""
        else:
            try:
                data = int(self.is_filled(context, data))
                self.field_data = data
                return self.field_data
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
    t_name: Field_
    t_type: Field_
    t_len: Field_
    t_sure: Field_


@dataclass
class Header:
    e_name: str
    tags: list[Tag]

    def _open_list_of_tags(self, tags: list[Tag]):
        tags = self.tags
        tag_dict = {}
        for item in tags:
            tag_dict[item.t_name] = {
                "type": item.t_type,
                "len": item.t_len,
                "sure": item.t_sure,
            }
        return tag_dict

    def build_dict(self):
        header_dict = {
            "header": {
                self.e_name: self._open_list_of_tags(self.tags)
            }
        }
        return header_dict
    
    def get_element_name(self, name):
        self.e_name = name

    def add_tag(self, tag: Tag):
        self.tags.append(tag)

    def build_yaml(self):
        header_dict = self.build_dict()
        header_yaml = as_document(header_dict)
        return header_yaml.as_yaml()
    
    def save_to_file(self, yaml_conf, file_name):
        with open(file_name, "w") as f:
            f.write(yaml_conf)

