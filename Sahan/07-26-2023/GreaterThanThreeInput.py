a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
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