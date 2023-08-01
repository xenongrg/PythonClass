a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b:
    if a > c:
        print(f"{a} is greater than {b} and {c}")
    else:
        print(f"{c} is greater than {a} and {b}")
else:
    if b > c:
        print(f"{b} is greater than {a} and {c}")
    else:
        print(f"{c} is greater than {a} and {b}")