def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


w = int(input("Enter number of series: "))

for i in range(w):
    print(fib(i))
