number1 = int(input("enter number 1: "))
number2 = int(input("enter number 2: "))

sum_of_numbers = 0
count_of_nubers = 0

for i in range(number1, number2 + 1):
    sum_of_numbers += i
    count_of_nubers += 1

average = sum_of_numbers / count_of_nubers

print(f"сумма чисел: {sum_of_numbers}")
print(f"середнє арифметичне: {average}")