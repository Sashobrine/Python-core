input_list = [7, 24, 75, 2, 0]


def summ_of_element(list):
    counter = 0
    for i in list:
        counter += i
    return counter


new_list = summ_of_element(input_list)
print(new_list)
