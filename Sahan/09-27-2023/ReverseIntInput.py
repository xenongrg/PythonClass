num = int(input("Enter number: "))
reverse = 0
while num > 0:
    remainder = num % 10  # Get the last digit
    reverse = (reverse * 10) + remainder  # Multiply previous remainder by 10 and add the last digit to reverse
    num = num // 10  # Remove the last digit

print(reverse)
