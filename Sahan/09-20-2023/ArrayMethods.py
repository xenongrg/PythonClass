cars = ["Ford", "Volvo", "BMW"]

for car in cars:       # to print an array
    print(car)

cars.append("Tesla")    # to add element in array
print("\nAfter append:")
for car in cars:
    print(car)

print("\n" + str(len(cars)))    # to print length of an array

cars.pop(1)     # to delete an array element with index
print("\nAfter pop:")
for car in cars:
    print(car)

cars.remove("Tesla")        # to delete an array element with value
print("\nAfter remove:")
for car in cars:
    print(car)

copy = cars.copy()        # prints copy of the list
print("\nCopy of cars:", copy)

x = cars.count("Ford")        # prints copy of the list
print("\nCount of selected value:",x)

cars2 = ["Mercedes", "Toyota"]
cars.extend(cars2)      # extends the list
print("\nNew List of Cars:")
for car in cars:
    print(car)

y = cars.index("Mercedes")      # prints index number of selected value
print("\nIndex number of selected value:",y)

cars.insert(1, "Suzuki")        # inserts new value according to index
print("\nNew List of Cars after insert:")
for car in cars:
    print(car)

cars.reverse()      # reverse the list of value
print("\nReversed list:")
for car in cars:
    print(car)

cars.sort()      # sorts A to Z
print("\nsorted list A to Z:")
for car in cars:
    print(car)

cars.sort(reverse=True)      # sorts Z to A
print("\nsorted list Z to A:")
for car in cars:
    print(car)
