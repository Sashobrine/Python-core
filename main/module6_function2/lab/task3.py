mix_list = [2, 4, 5, -98, -15, -79, -54, 7]


def counter_of_list(lst):
    neg_num = 0
    pos_num = 0
    even_num = 0
    odd_num = 0

    for i in lst:
        if i >= 0:
            pos_num += 1
        elif i < 0:
            neg_num += 1

        if i % 2 == 0:
            even_num += 1
        else:
            odd_num += 1

    return neg_num, pos_num, even_num, odd_num


result_tuple = counter_of_list(mix_list)
print(result_tuple)
