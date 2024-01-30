start_number = int(input("enter number1 : "))
end_number = int(input("enter number2 : "))

for i in range(start_number, end_number + 1):
    if i % 5 == 0 & i % 3 == 0:
        print("Fizz Buzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
