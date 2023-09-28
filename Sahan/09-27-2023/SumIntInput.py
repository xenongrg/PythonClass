num = int(input("Enter number: "))
digit_sum = 0
while num > 0:
    remainder = num % 10  # Get the last digit
    digit_sum = digit_sum + remainder  # Add the last digit to digit_sum
    num = num // 10  # Remove the last digit

print(digit_sum)
