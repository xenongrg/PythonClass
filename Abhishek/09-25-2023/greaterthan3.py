def compare(a, b):
    comparison = a > b
    return comparison


x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = int(input("Enter 3rd number: "))
if compare(x, y):
    if compare(x, z):
        print(f"{x} = a is greater")
    else:
        print(f"{z} = c is greater")
else:
    if compare(y, z):
        print(f"{y} = b is greater")
    else:
        print(f"{z} = c is greater")
