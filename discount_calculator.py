purchase_amount= int(input("Enter purchase amount "))
discount=0
total_bill=0
if purchase_amount>3000:
    d=25
    total_bill=purchase_amount
    discount=(purchase_amount*d)/100
    total_bill-=discount
    print("your purchase amount is ",purchase_amount)
    print("you got ",d,"% discount")
    print("your total bill amount after discount is ",total_bill)
elif purchase_amount>2000 and purchase_amount<=3000:
    d = 20
    total_bill = purchase_amount
    discount = (purchase_amount * d) / 100
    total_bill -= discount
    print("your purchase amount is ", purchase_amount)
    print("you got ", d, "% discount")
    print("your total bill amount after discount is ", total_bill)
elif purchase_amount>1000 and purchase_amount<=2000:
    d = 10
    total_bill = purchase_amount
    discount = (purchase_amount * d) / 100
    total_bill -= discount
    print("your purchase amount is ", purchase_amount)
    print("you got ", d, "% discount")
    print("your total bill amount after discount is ", total_bill)
else:
    total_bill=purchase_amount
    print("you got no discount")
    print("To be eligible for discount your purchase amount should be greater than 1000")
    print("You purchase amount is rs ",purchase_amount)
    print("your total bill is ",total_bill)

