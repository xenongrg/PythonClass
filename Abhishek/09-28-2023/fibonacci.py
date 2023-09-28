def fibonacci(a, b, c):
    for i in range(a):
        print(b)
        n = b + c
        b = c
        c = n
    return a


r = int(input("Enter nth number: "))
x = 0
y = 1
fibonacci(r, x, y)



# without function
# r = int(input("Enter nth number: "))
# x = 0
# y = 1
# for i in range(r):
#     print(x)
#     n = x + y
#     x = y
#     y = n
