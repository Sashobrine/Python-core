input_list = [1, 2, 4, 6, 8]


def summ_of_element(list):
    counter = 1
    for i in list:
        counter *= i
    return counter


new_list = summ_of_element(input_list)
print(new_list)
