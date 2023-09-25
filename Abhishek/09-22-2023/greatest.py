numbers = []    # making a null array to store the numbers
print("Enter 1st integer: ")        # taking 1st integer
a = int(input())

print("Enter 2nd integer: ")        # taking 2nd integer
b = int(input())

print(f'Two integers are {a},{b}')

numbers.append(a)           # making the integers into array
numbers.append(b)           # making the integers into array
print("Numbers in array: ", numbers)
numbers.sort()              # sorting to take out the index and finding the greater value
print(numbers)
if numbers[1]:                  # condition to check the greatest number
    print("This number is greater: ", numbers[1])
else:
    print("This number is greater: ", numbers[0])
