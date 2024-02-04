number = 123420


def lucky_num(num):
    test_list = [int(i) for i in str(num)]
    sum_list1 = sum(test_list[:3])
    sum_list2 = sum(test_list[-3:])
    if sum_list1 == sum_list2:
        return True
    else:
        return False


result = lucky_num(number)
print(lucky_num(number))
