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
