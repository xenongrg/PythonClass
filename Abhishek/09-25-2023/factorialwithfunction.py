def factorial(a, b):
    for x in range(a, 0, -1):
        b = b * x
    return b


# factorial
print("Enter the number: ")
number = int(input())
factorial_value = 1
result = factorial(number, factorial_value)
print(f'Factorial is {result}')
