car_list = [["BMW1", "BMW2", "BMW3"], ["Ford1", "Ford2", "Ford3"], ["Tesla1", "Tesla2", "Tesla3"]]
i = 0
while i < len(car_list):
    j = 0
    while j < len(car_list[i]):
        k = 0
        while k < len(car_list[i][j]):
            print(car_list[i][j][k])
            k = k+1
        j = j+1
    i = i+1
