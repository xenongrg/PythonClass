name1 = input("Enter 1st person's name: ")
salary1 = int(input("Enter 1st person's salary: "))
name2 = input("Enter 2nd person's name: ")
salary2 = int(input("Enter 2nd person's salary: "))
name3 = input("Enter 3rd person's name: ")
salary3 = int(input("Enter 3rd person's salary: "))

if salary1 >= 100000:
    salary1 = salary1 - (salary1 * 0.1)
if salary2 >= 100000:
    salary2 = salary2 - (salary2 * 0.1)
if salary3 >= 100000:
    salary3 = salary3 - (salary3 * 0.1)

print(name1, salary1)
print(name2, salary2)
print(name3, salary3)