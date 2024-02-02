new_list = [2, 5, 11, 17, 23, 29, 37, 2, 5, 11, 17, 23, 29, 37, 2, 5, 11, 17, 23, 29, 37, 2, 5, 11, 17, 23, 29, 37, ]
num_to_del = 2


def count_of_num(list, num):
    count = 0
    for i in list:
        if i == num:
            count += 1
    return count


list = [i for i in new_list if i != num_to_del]
del_nums = count_of_num(new_list, num_to_del)

print(del_nums)
print(list)