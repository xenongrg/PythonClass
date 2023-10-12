def find_y(m, c):
    return lambda x: m * x + c


m1 = 1
c1 = 2
x1 = []
for i in range(3):
    x1.append(int(input(f"Enter values of x{i + 1}: ")))

y1 = []
y = find_y(m1, c1)

for i in x1:
    y1.append(y(i))

print("-----------------")
print("| x |", end=" ")
for i in x1:
    print(i, "| ", end="")
print("\n|---|---|---|---|")
print("| y |", end=" ")
for j in y1:
    print(j, "| ", end="")
print("\n-----------------")
