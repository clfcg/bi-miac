from strictyaml import load

from bi_miac.configs.base_conf import CONF_HEADER
from bi_miac.bi_cmd.elements import Header, Tag, Field_


def get_header_conf():
    yaml = load(CONF_HEADER.read_text()).data
    
    tag_list = []
    for elements in yaml.values():
        for elemement, tags in elements.items():
            element_name = elemement
            for tag, options in tags.items():
                tag_name = tag
                options = list(options.values())
                tag_obj = Tag(tag_name, options[0], options[1], options[2])
                tag_list.append(tag_obj)

    header = Header(element_name, tag_list)
    return header

def add_header_tags():
    header = get_header_conf()

    command = ""
    while command.lower() != "n":
        tag_name = Field_().is_filled("Имя реквизита")
        if tag_name not in [tag.t_name for tag in header.tags]:
            tag_type = Field_().get_type_field("Тип реквизита")
            tag_length = Field_().get_length_field("Размер реквизита", tag_type)
            tag_sure = Field_().get_fsure_field("Обязательность реквизита(0-нет, 1-да)")

            tag = Tag(tag_name, tag_type, tag_length, tag_sure)
            header.add_tag(tag)
            print(f"\033[1;34mРеквизит {tag_name} добавлен\033[0m\n")
            command = input("Добавить еще реквизит? [y/n]: ")
        else:
            print(f"\033[1;31mРеквизит {tag_name} уже существует\033[0m\n")
            command = input("Добавить еще реквизит? [y/n]: ")

    yaml = header.build_yaml()
    header.save_to_file(yaml, CONF_HEADER)