start_num = 9
end_num = -700


def sum_of_range(start, end):
    result = 0
    if start_num < end:
        for i in range(start, end + 1):
            result += i
        return result
    else:
        for i in range(start, end, -1):
            result += i
        return result


result_sum = sum_of_range(start_num, end_num)
print(result_sum)
