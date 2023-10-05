x = int(input("Enter a number : "))
rev = 0
temp = x
while x > 0:
    rev = (rev * 10) + x % 10
    x = x//10
if rev == temp:
    print("This is palindrome")
else:
    print("This is not palindrome")



