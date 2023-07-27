User1Salary = int(input("Enter Salary1: "))
User1Name = input("Enter First name1: ")
User2Salary = int(input("Enter Salary2: "))
User2Name = input("Enter First name2: ")
User3Salary = int(input("Enter Salary3: "))
User3Name = input("Enter First name3: ")
if User1Salary >= 100000:
    x = User1Salary - (User1Salary * 0.1)
    print(User1Name, "earns", x)
else:
    print(User1Name, "earns", User1Salary)
if User2Salary >= 100000:
    y = User2Salary - (User2Salary * 0.1)
    print(User2Name, "earns", y)
else:
    print(User2Name, "earns", User2Salary)
if User3Salary >= 100000:
    z = User3Salary - (User3Salary * 0.1)
    print(User3Name, "earns", z)
else:
    print(User3Name, "earns", User3Salary)