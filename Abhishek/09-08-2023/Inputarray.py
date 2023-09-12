lst = []

n = int(input("Enter number of elements : "))
print("Enter " + str(n) + " elements:\n")
for i in range(0, n):
    ele = input()
    lst.append(ele)

print(lst)

###another one
value = input("Enter values separated by commas: ")
print("Array:", value.split(','))
