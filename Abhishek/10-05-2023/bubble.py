x = [5, 4, 3, 2, 1]
i = 0
while i <= len(x) - 2:
    j = 0
    while j <= (len(x)) - i - 2:
        if x[j] > x[j + 1]:
            temp = x[j + 1]
            x[j + 1] = x[j]
            x[j] = temp
        j = j + 1
        print(x)
    i = i + 1


# for i in range(6):
#     for j in range(6 - i):
#         if x[j] > x[j + 1]:
#             temp = x[j + 1]
#             x[j + 1] = x[j]
#             x[j] = temp
#             print(x)
