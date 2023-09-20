cost_price = int(input("Enter cost: "))
marked_price = int(input("Enter marked price: "))
discount = int(input("Enter discount: "))
vat = int(input("Enter VAT: "))

discounted_price = marked_price - (discount/100*marked_price)
selling_price = discounted_price+(vat/100*discounted_price)
difference = selling_price - cost_price

if difference == 0:
    print("Neither profit nor loss")
else:
    if difference > 0:
        print("Profit is : ", difference)
    else:
        print("Loss is : ", difference)

