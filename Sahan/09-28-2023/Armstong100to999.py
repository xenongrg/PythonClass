for i in range(1, 1000):
    x = i
    result = 0
    while x > 0:
        reminder = x % 10
        result = result + (reminder * reminder * reminder)
        x = x // 10
    if i == result:
        print(i)
