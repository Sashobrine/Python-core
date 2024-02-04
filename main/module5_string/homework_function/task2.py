number1 = 5
number2 = -67


def negative_numbers(num1, num2):
    new_list = []
    if num1 < num2:
        for i in range(num1, num2):
            if i % 2:
                new_list.append(i)
    else:
        for i in range(num1, num2, -1):
            if i % 2:
                new_list.append(i)
    return new_list


print(negative_numbers(number1, number2))
