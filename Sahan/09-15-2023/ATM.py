pin = int(5456)
balance = int(50000)
pin_input = int(input("Enter pin: "))

if pin_input == pin:
  amount = int(input("Enter amount to withdraw: "))

  while amount <= balance:
    remaining_balance = balance-amount
    print("Please collect your cash. Your remaining balance:",remaining_balance)
    withdraw_again = input("Would you like to withdraw again? Enter Y for Yes and N for No: ")
    if withdraw_again == "Y":
      new_amount = int(input("Enter amount to withdraw: "))
      if new_amount <= remaining_balance:
        balance = balance - new_amount
      else:
        print("Insufficient Balance")
        break
    else:
        print("Thank You!")
        break
  else:
    print("Insufficient Balance")
else:
    print("Incorrect Pin")
