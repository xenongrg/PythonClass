num = 0
for i in range(0, 5):
    for j in range(0, 5 - i):
        if num < 9:
            print(num+1, end="      ")
        else:
            print(num+1, end="     ")
        num = num + 1
    print()

