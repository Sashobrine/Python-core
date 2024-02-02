list_first = [2, 3, 4, 5, 6, "SASHA", "ANDREY", "VOVA", "BOGAN"]
list_second = ["SASHA", "ANDREY", "VOVA", "BOGAN", 4, 6, 7, 8, 9]


def united_list(list1, list2):
    list = list1 + list2
    return list


new_list = united_list(list_first, list_second)
print(new_list)
