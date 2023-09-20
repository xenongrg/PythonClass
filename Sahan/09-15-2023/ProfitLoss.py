cost_price = int(input("Enter Cost Price: "))
marked_price = int(input("Enter Marked Price: "))
discount = int(input("Enter Discount Percent: "))
vat = int(input("Enter VAT Percent: "))

discounted_price = marked_price-(discount/100*marked_price)
selling_price = discounted_price+(vat/100*discounted_price)
difference = selling_price-cost_price
if difference == 0:
     print("Neither Profit Nor Loss")
else:
    if difference > 0:
        print("Profit is:", difference)
    else:
        print("Loss is:", difference)
