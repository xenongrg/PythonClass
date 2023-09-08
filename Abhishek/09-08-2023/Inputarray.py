lst = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = str(input())
    lst.append(ele)

print(lst)

###another one
value = input("Enter values separated by commas: ")
print("Array:", value.split(','))