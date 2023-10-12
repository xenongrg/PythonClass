x = [5, 4, 3, 2, 1]
i = 0
while i < len(x) - 1:
    j = i + 1
    while j > 0:
        if x[j] < x[j - 1]:
            temp = x[j - 1]
            x[j - 1] = x[j]
            x[j] = temp
        else:
            break
        j = j - 1
        print(x)
    i = i + 1

    # print(x)
