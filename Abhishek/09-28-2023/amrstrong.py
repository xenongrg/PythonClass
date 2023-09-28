x = int(input("Enter a 3 digit number: "))
n = x
armstrong = 0
while x > 0:
    armstrong = armstrong + (x % 10)*(x % 10)*(x % 10)
    x = x//10
print(n)
print(armstrong)
if n == armstrong:
    print("This is armstrong number")
else:
    print("This is not armstrong number")

