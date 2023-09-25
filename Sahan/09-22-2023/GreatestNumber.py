x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x - y != abs(x - y):
    print(f'Greatest number is {y}')
elif y - x != abs(y - x):
    print(f'Greatest number is {x}')
else:
    print("Both numbers are equal.")
