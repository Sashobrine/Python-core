input_list = [1, 2, 3, 4, 5, 6, 7, 8]


def every_nums_to_factorial(list):
    new_list = []
    for i in list:
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        new_list.append(factorial)
    return new_list

    # new_list = [[i * i for i in range(j)] for j in list]


result_list = every_nums_to_factorial(input_list)
print(result_list)
