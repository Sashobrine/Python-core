start_number = int(input("enter number1 : "))
end_number = int(input("enter number2 : "))

count_of_numbers = 0

print(f"Всі числа діапазону: ")
for i in range(start_number, end_number + 1):
    print(i, end=" ")
print()

print(f"\nВсі числа діапазону в спадному порядку: ")
for i in range(end_number, start_number - 1, -1):
    print(i, end=" ")
print()

print(f"\nВсі числа, кратні 7: ")
for i in range(start_number, end_number + 1):
    if i % 7 == 0:
        print(i, end=" ")
print()

print(f"\nКількість чисел, кратних 5: ")
for i in range(start_number, end_number + 1):
    if i % 5 == 0:
        count_of_numbers += 1
print(count_of_numbers, end=" ")


