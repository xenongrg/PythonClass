x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = int(input("Enter 3rd number: "))
if x > y:
    if x > z:
        print(f"{x} is greater")
    else:
        print(f"{z} is greater")
else:
    if y > z:
        print(f"{y} is greater")
    else:
        print(f"{z} is greater")