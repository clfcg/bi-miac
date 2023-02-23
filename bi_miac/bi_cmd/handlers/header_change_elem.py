import strictyaml as sy

from bi_miac.configs.base_conf import CONF_HEADER
from bi_miac.bi_cmd.elements import Header, Tag, Field_


def get_header_conf():
    yaml = sy.load(CONF_HEADER.read_text()).data
    
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


def change_header_element_name():
    header = get_header_conf()
    kw = Field_().is_filled("Предыдущее имя элемента")
    if kw == header.e_name:
        new_element_name = Field_().is_filled("Новое имя элемента")
        header.get_element_name(new_element_name)
        yaml = header.build_yaml()
        header.save_to_file(yaml, CONF_HEADER)
        print(f"Имя элемента изменено \033[1;31m{kw}\033[0m -> "
              f"\033[1;34m{new_element_name}\033[0m\n")
    else:
        print(f"\033[1;31mЭлемент {kw} не найден\033[0m\n")