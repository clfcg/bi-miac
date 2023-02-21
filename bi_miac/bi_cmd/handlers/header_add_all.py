from pathlib import Path

import strictyaml as sy

from bi_miac.bi_cmd.elements import Field_, Tag, Header
from bi_miac.configs.base_conf import CONF_DIR


def get_header():
    command = ""
    tag_list = []
    element_name = Field_().is_filled("Имя элемента")

    while command.lower() != "n":
        tag_name = Field_().is_filled("Имя реквизита")
        tag_type = Field_().get_type_field("Тип реквизита")
        tag_length = Field_().get_length_field("Размер реквизита", tag_type)
        for_sure = Field_().get_fsure_field("Обязательность реквизита(0-нет, 1-да)")

        tag = Tag(tag_name, tag_type, tag_length, for_sure)
        tag_list.append(tag)
        command = input("Добавить еще реквизит? [y/n]: ")
    
    header_data = Header(element_name, tag_list)
    header_dict = header_data.build_dict()
    return header_dict


def create_header(header_struct: dict):
    yaml = sy.as_document(header_struct)
    return yaml.as_yaml()


def write_header_yaml():
    header = get_header()
    yaml_header = create_header(header)
    file = CONF_DIR / "header.yaml"
    with open(file, "w") as f:
        f.write(yaml_header)


def add_full_header():
    file = CONF_DIR / "header.yaml"
    if file.stat().st_size != 0:
        yaml = sy.load(file.read_text()).data
        yaml = sy.as_document(yaml)
        print("\033[1;31mСтруктура заголовка существует:\033[0m:\n")
        print(yaml.as_yaml())

        question = ""
        while question not in ["y", "n"]:
            question = input("Хотите перезаписать структуру заголовка? [y/n]: ")
        else:
            if question.lower() == "y":
                write_header_yaml()
            elif question.lower() == "n":
                pass
    else:
        write_header_yaml()