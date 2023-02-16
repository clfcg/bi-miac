import strictyaml as sy

from bi_miac.bi_cmd.elements import Tag, Header


def get_all_header():
    kw = ""
    tag_list = []
    elem_name = input("Имя элемента: ")
    while kw.lower() != "n":
        t_name = input("Имя реквизита: ")
        t_type = input("Тип реквизита: ")
        t_len = int(input("Размер реквизита: "))
        t_sure = bool(input("Обязательность реквизита(0-нет, 1-да): "))
        tag = Tag(t_name, t_type, t_len, t_sure)
        tag_list.append(tag)
        kw = input("Добавить еще реквизит? [y/n]: ")
    
    header = Header(elem_name, tag_list)
    print(header)

get_all_header()



