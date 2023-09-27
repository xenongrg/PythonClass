def fact(a, b):
    for x in range(a, 0, -1):
        b = b * x
    return b


n = int(input("Enter number: "))
mult = 1
result = fact(n, mult)
print(f'Factorial of {n} is {result}')
