input_text = input("enter text: ")


def count_text(text):
    count = 0
    for i in text:
        if i in ['!', '.', '?']:
            count += 1
    return count


result = count_text(input_text)
print(result)
