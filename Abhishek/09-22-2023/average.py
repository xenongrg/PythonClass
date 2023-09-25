# average
array = []
n = 5
print("Enter the 5 numbers :")
for i in range(0,n):
    array.append(int(input()))
summation = 0
for element in array:
    summation = summation + element
print(f'average = {summation/n}')

# factorial
print("Enter the number: ")
number = int(input())
factorial = 1
for x in range(number, 0, -1):
    factorial = factorial * x
print(f'Factorial is {factorial}')


