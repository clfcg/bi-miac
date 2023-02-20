import strictyaml as sy

from bi_miac.bi_cmd.elements import Field_, Tag, Header
from bi_miac.bi_cmd.handlers.all_check_types import check_type, set_len, check_data_filled


def get_header():
    command = ""
    element_name = Field_().is_filled("Имя элемента")

    while command.lower() != "n":
        tag_name = Field_().is_filled("Имя реквизита")
        tag_type = Field_().get_type_field("Тип реквизита")
        tag_length = Field_().get_length_field("Размер реквизита", tag_type)
        for_sure = Field_().get_fsure_field("Обязательность реквизита(0-нет, 1-да)")
        
        command = input("Добавить еще реквизит? [y/n]: ")
    
    print(element_name, tag_name, tag_type, tag_length, for_sure)
    

get_header()





def get_all_header():
    kw = ""
    flag = False
    tag_list = []
    elem_name = check_data_filled(input("Имя элемента: "))
    while kw.lower() != "n":
        t_name = input("Имя реквизита: ")
        while flag != True:
            t_type = input("Тип реквизита: ")
            flag = check_type(t_type)
        if set_len(t_type):
            t_len = int(input("Размер реквизита: "))
        else:
            t_len = None
        t_sure = bool(int(input("Обязательность реквизита(0-нет, 1-да): ")))
        tag = Tag(t_name, t_type, t_len, t_sure)
        tag_list.append(tag)
        flag = False
        kw = input("Добавить еще реквизит? [y/n]: ")
    
    header = Header(elem_name, tag_list)
    print(header)