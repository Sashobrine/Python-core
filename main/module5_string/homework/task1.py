input_str = str(input("Enter your text: "))


def check_text(string):
    reversed_str = string[::-1]
    if string == reversed_str:
        print('Так, цей рядок є паліндром')
    else:
        print('Ні, цей рядок не є паліндром')


check_text(input_str)
