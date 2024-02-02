list_of_num = [2, 3, 4, 5, 6, 7, 8]
n = 2


def multiplicative_nums(list, degree):
    new_list = [i ** degree for i in list]
    return new_list


result_list = multiplicative_nums(list_of_num, n)
print(result_list)