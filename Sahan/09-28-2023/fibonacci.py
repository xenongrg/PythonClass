# n = int(input("Enter number of series: "))
# x = 0
# y = 1
# print(f'{x}, {y}', end="")
#
# for i in range(n - 2):
#     new = x + y
#     print(f', {new}', end="")
#     x = y
#     y = new

x = 0
y = 1
for i in range(10):
    n = x
    x = x + y
    y = n
    print(n)

# x = 0
# y = 1
# for i in range(10):
#     print(x)
#     n = x + y
#     x = y
#     y = n
