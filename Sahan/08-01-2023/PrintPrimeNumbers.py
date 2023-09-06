i = 2

while i <= 100:
    j = 2
    while j <= i:
        if i % j == 0:
            break
        j = j + 1
    if i == j:
        print(i)
    i = i + 1
