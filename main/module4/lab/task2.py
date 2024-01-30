number = int(input("enter number : "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f"факторіал числа {number} буде: {factorial}")

a = int(input("enter number : "))


def factorial(a):
    result = 1
    for i in range(1, a + 1):
        result *= i
    return result


print(f"факторіал числа {a} буде:  {factorial(a)}")
