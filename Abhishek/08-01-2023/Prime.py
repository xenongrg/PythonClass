i = 1

while i <= 100:
    j=2
    while j < 100:
        if i%j == 0:
            break
        j += 1
    if  i == j:
        print(i)
    i += 1
