x = int(input("Enter a number : "))
summation = 0
while x > 0:
    summation = summation + x % 10
    x = x//10
print("Sum of digits in a number: ", summation)

