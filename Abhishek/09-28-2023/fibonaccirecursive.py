def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i - 1) + fibonacci(i - 2)


r = int(input("Enter nth number: "))
for a in range(r):
    print(fibonacci(a))
