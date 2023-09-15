x = int(input("Enter a number: "))
is_prime = True
i = 2
if x % i == 0:
    is_prime = False
else:
    i = i + 1
    while i <= x/2:
        if x % i == 0:
            is_prime = False
            break
        i = i + 2

if is_prime:
    print("Prime")
else:
    print("Not Prime")
