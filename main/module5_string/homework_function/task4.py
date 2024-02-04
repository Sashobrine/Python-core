number1 = 912
number2 = 34
number3 = 31
number4 = 82


# def max_num(num1, num2, num3, num4):
#     list = [num1, num2, num3, num4]
#     list.sort()
#     return list[-1]
#

def max_num(num1, num2, num3, num4):
    list = [num1, num2, num3, num4]
    return max(list)


result = max_num(number1, number2, number3, number4)
print(result)
