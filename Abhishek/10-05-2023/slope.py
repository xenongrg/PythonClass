def slope_intercept_form(slope, y_intercept):
    return lambda x: slope * x + y_intercept


m = 1
c = 2
x1 = []
for i in range(3):
    x1.append(int(input(f"Enter the value of x{i + 1}:")))

y1 = []
y = slope_intercept_form(m, c)

for i in x1:
    y1.append(y(i))

print("...................")
print("| x:", "|", end="\t")
i = 0
for i in x1:
    print(i, "|", end="\t")
print()
print("...................")
print("| y:", "|", end="\t")
i = 0
for i in y1:
    print(i, "|", end="\t")
print()
print("...................")

