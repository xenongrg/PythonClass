x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = int(input("Enter 3rd number: "))
if x>y and x>z:
    print(x," is the greater one")
elif y>x and y>z:
    print(y," is the greater one")
else:
    print(z," is the greater one")