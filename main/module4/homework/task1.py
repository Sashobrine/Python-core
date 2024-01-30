start_number = int(input("enter number1 : "))
end_number = int(input("enter number2 : "))


for i in range(start_number, end_number + 1):
    if i % 7 == 0:
        print(i, end=" ")
