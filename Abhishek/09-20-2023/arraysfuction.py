
fruits = ["Orange", "Apple", "Mango", "Pineapple", "Kera"]
fruits.append("Kera")
print(fruits)

fruits.copy()
print(fruits)

fruits.clear()
print(fruits)

fruits = ["Orange", "Apple", "Mango", "Pineapple", "Kera", "Kera"]
print(fruits.count("Kera"))

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

fruits = ["Orange", "Apple", "Mango", "Pineapple", "Kera", "Kera"]
print(fruits.index("Kera"))

fruits = ["Orange", "Apple", "Mango", "Pineapple", "Kera", "Kera"]
fruits.insert(2, "KERA3")
print(fruits)

fruits = ["Orange", "Apple", "Mango", "Pineapple", "Kera", "Kera"]
fruits.pop(3)
print(fruits)

fruits = ["Orange", "Apple", "Mango", "Pineapple", "Kera", "Kera"]
fruits.remove("Orange")
print(fruits)

fruits = ["Orange", "Apple", "Mango", "Pineapple", "Kera", "Kera"]
fruits.reverse()
print(fruits)

fruits = ["Orange", "Apple", "Mango", "Pineapple", "Kera", "Kera"]
fruits.sort()
print(fruits)
