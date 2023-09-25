def compare(a, b):
    comparison = a > b
    return comparison


def compare1(a, c):
    comparison1 = a > c
    return comparison1


def compare2(b, c):
    comparison2 = b > c
    return comparison2


x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = int(input("Enter 3rd number: "))
if compare(x, y):
    if compare1(x, z):
        print(f"{x} = a is greater")
    else:
        print(f"{z} = c is greater")
else:
    if compare2(y, z):
        print(f"{y} = b is greater")
    else:
        print(f"{z} = c is greater")
