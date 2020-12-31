no_of_units_consumed=int(input("Enter the number of units that are consumed"))
cost_per_unit=0
current_bill=0
if no_of_units_consumed>200:
    cost_per_unit=15
    current_bill=no_of_units_consumed*cost_per_unit
    print("you have consumed ",no_of_units_consumed," units")
    print("your bill amount is ",current_bill)
elif no_of_units_consumed>150 and no_of_units_consumed<=200:
    cost_per_unit=12
    current_bill = no_of_units_consumed * cost_per_unit
    print("you have consumed ", no_of_units_consumed, " units")
    print("your bill amount is ", current_bill)
elif no_of_units_consumed>100 and no_of_units_consumed<=150:
    cost_per_unit=9
    current_bill = no_of_units_consumed * cost_per_unit
    print("you have consumed ", no_of_units_consumed, " units")
    print("your bill amount is ", current_bill)
elif no_of_units_consumed>50 and no_of_units_consumed<=100:
    cost_per_unit=6
    current_bill = no_of_units_consumed * cost_per_unit
    print("you have consumed ", no_of_units_consumed, " units")
    print("your bill amount is ", current_bill)
else:
    cost_per_unit=3
    current_bill = no_of_units_consumed * cost_per_unit
    print("you have consumed ", no_of_units_consumed, " units")
    print("your bill amount is ", current_bill)