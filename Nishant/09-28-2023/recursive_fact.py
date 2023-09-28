def factorial(x):
    if x == 1:
        return 1
    result = x * factorial(x-1)
    return result


n = int(input("Enter a number: "))
print(f'Factorial of {n} = {factorial(n)}')
