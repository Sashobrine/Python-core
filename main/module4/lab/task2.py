number = int(input("enter number : "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f"факторіал числа {number} буде: {factorial}")