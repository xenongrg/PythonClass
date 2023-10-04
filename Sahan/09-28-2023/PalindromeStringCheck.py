a = str(input("Enter a word: "))
b = a[::-1]

if a == b:
    print(f"{a} is a Palindrome word")
else:
    print(f"{a} is not a Palindrome word")
