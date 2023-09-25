def comp1(a, b):
    greater1 = a > b
    return greater1


def comp2(a, c):
    greater2 = a > c
    return greater2


def comp3(b, c):
    greater3 = b > c
    return greater3


x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = int(input("Enter 3rd number: "))
if comp1(x, y):
    if comp2(x, z):
        print(f"{x} is greater")
    else:
        print(f"{z} is greater")
else:
    if comp3(y, z):
        print(f"{y} is greater")
    else:
        print(f"{z} is greater")
