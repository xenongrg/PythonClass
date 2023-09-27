i = 0
n = 1
while i < 4:
    j = 0
    while j < 3 - i:
        print(" ", end=" ")
        j = j + 1
    k = 0
    while k < i + 1:
        print(n, " ", end=" ")
        n = n + 1
        k = k + 1
    print()
    i = i + 1
