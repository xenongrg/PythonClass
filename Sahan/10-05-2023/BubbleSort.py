a = [8, 10, -6, 5, 4]
for i in range(4):
    for j in range(4 - i):
        if a[j] > a[j + 1]:
            temp = a[j + 1]
            a[j + 1] = a[j]
            a[j] = temp
print(a)
