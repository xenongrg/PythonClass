intList = []
number = 5
print("Enter 5 numerical values\n")
for i in range(number):
    intList.append(int(input()))
print(intList)

summation = 0
for element in intList:
    summation = summation + element
print(f'Average = {summation/number}')

mult = 1
for x in range(number, 0, -1):
    mult = mult * x
print(f'Factorial of {number} is {mult}')
