input_text = str(input('Enter a text: '))
input_str = input('Enter a list: ')


def format_text(text, my_list):
    new_text = text
    str_to_list = [item.strip() for item in my_list.split(',')]

    for i in str_to_list:
        if i in new_text:
            new_text = new_text.replace(i, i.upper())

    return new_text


mat_text = format_text(input_text, input_str)
print(mat_text)

# don`t work