lst = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = str(input())
    lst.append(ele)

print(lst)

###another one
input_str = input("Enter values separated by commas: ")
input_list = input_str.split(',')

input_list = [item.strip() for item in input_list]

print("Array:", input_list)