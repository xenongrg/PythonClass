a = [9, 8, 5, 3, 2]
for j in range(4):
    if a[j + 1] < a[j]:
        temp = a[j + 1]
        a[j + 1] = a[j]
        a[j] = temp
        for i in range(j):
            if a[j - i] < a[j - i - 1]:
                temp2 = a[j - i]
                a[j - i] = a[j - i - 1]
                a[j - i - 1] = temp
print(a)
