arr = [9, 3, 8, -5, 2]

for i in range(4):
    small = i
    for j in range(i + 1, 5):
        if arr[j] < arr[small]:
            small = j

    if i != small:
        temp = arr[i]
        arr[i] = arr[small]
        arr[small] = temp

print(arr)
