def concat_list(str_list) -> str:
    str = ""
    for s in str_list:
        str = str + " " + s
    return str

def concat_list_prefix(str_list, prefix) -> str:
    str = ""
    for s in str_list:
        str = str + " " + prefix + s

    return str