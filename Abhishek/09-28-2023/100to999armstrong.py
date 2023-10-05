for i in range(100, 1000):
    x = i
    armstrong = 0
    while x > 0:
        armstrong = armstrong + (x % 10)**3
        x = x // 10

    if i == armstrong:
        print(armstrong, end=",")

