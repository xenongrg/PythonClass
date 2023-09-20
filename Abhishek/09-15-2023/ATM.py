USER_PIN = int(1234)

TOTAL_AMOUNT = int(100000)
pin = int(input("Enter your pin: "))

if pin == USER_PIN:
    amount = int(input("Enter the amount you want to withdraw: "))

    while amount <= TOTAL_AMOUNT:
        current_amount = TOTAL_AMOUNT - amount
        print("Your Current Amount: ", current_amount)
        with_draw_again = input("Do you want to perform more transactions?\n Y for Yes or N for No\n")
        if with_draw_again == "Y":
            new_amount = int(input("Enter the amount you want to withdraw: "))
            if new_amount <= current_amount:
                TOTAL_AMOUNT = TOTAL_AMOUNT - new_amount
            else:
                print("Insufficient fund")
                break
        else:
            print("Thank you!")
            break
    # else:
    #     print()
else:
    print("Please try again.")
