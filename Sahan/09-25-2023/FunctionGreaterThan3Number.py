def comp(a, b):
    greater1 = a > b
    return greater1


x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = int(input("Enter 3rd number: "))
if comp(x, y):
    if comp(x, z):
        print(f"{x} is greater")
    else:
        print(f"{z} is greater")
else:
    if comp(y, z):
        print(f"{y} is greater")
    else:
        print(f"{z} is greater")
