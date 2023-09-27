i = 0
m = 1
while i < 4:
    j = 1
    while j <= 3 - i:
        print(" ", end=" ")
        j = j + 1
    k = 1

    while k <= i + 1:
        print(m, " ", end=" ")
        m = m + 1
        k = k + 1

print()
i = i + 1
