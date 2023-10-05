a = [2, 8, 5, 3, 9]
for j in range(4):
    if a[j + 1] < a[j]:
        temp = a[j + 1]
        a[j + 1] = a[j]
        a[j] = temp
        for i in range(j):
            if a[j] < a[j - 1]:
                temp2 = a[j]
                a[j] = a[j - 1]
                a[j - 1] = temp
print(a)
