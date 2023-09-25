numbers = []    # null matrix
print("Enter 1st integer: ")        # taking 1st integer
a = int(input())

print("Enter 2nd integer: ")        # taking 2nd integer
b = int(input())

numbers.append(a)   # putting int in matrix
numbers.append(b)
print(numbers)
numbers.reverse()   # reversing the values
print(numbers)
a = numbers[0]      # swapping values in matrix
b = numbers[1]      # swapping values in matrix
print(a)
print(b)
