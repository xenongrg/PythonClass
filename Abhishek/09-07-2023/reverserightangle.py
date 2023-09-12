i = 1
num = 1
while i <= 5:
    j = 1
    while j <= 6 - i:
        if num <= 9:
            print(num, end="   ")
        else:
            print(num, end="  ")
        num = num + 1
        j = j + 1
    print()
    i = i + 1
