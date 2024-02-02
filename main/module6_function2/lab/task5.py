input_list = [2, 6, 4, 5, -98, 6, -15, -79, 6, -54, 7, 6]
num_to_find = 6


def find_numbs(list, n):
    return n in list


result = find_numbs(input_list, num_to_find)
print(result)
