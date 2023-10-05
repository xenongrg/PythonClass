x = int(input("Enter 3 digit number: "))
n = x
result = 0
while x > 0:
    reminder = x % 10
    result = result + reminder ** 3
    x = x // 10
if result == n:
    print("It is an armstrong number.")
else:
    print("It is not an armstrong number.")
