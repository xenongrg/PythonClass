name1 = input("Enter 1st person's name: ")
salary1 = int(input("Enter 1st person's salary: "))
name2 = input("Enter 2nd person's name: ")
salary2 = int(input("Enter 2nd person's salary: "))
name3 = input("Enter 3rd person's name: ")
salary3 = int(input("Enter 3rd person's salary: "))
if salary1 >= 100000:
    print(name1, salary1 - (salary1 * 0.1))
else:
    print(name1, salary1)
if salary2 >= 100000:
    print(name2, salary2 - (salary2 * 0.1))
else:
    print(name2, salary2)
if salary3 >= 100000:
    print(name3, salary3 - (salary3 * 0.1))
else:
    print(name3, salary3)