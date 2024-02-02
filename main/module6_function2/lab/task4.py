input_list = [2, 5, "11", 17, 23, 29, 37, 25]


def reversed_list(list):
    return list[::-1]


# def reversed_list(list):
#     new_list = list
#     new_list.reverse()
#     return new_list


result_list = reversed_list(input_list)
print(result_list)
