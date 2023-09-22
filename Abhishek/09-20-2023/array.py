cars = [["bmw1", "bmw2", "bmw3"], ["volvo1", "volvo2", "volvo3"], ["ford1", "ford2", "ford3"]]

i = 0
while i < len(cars):
    j = 0
    while j < len(cars[i]):
        k = 0
        while k < len(cars[i][j]):
            print(cars[i][j][k])

            k += 1

        j += 1
    i += 1
