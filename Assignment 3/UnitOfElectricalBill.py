unit = float(input("Enter unit: "))
El = 0 

if(unit > 0):
    if(unit<=50):
        El = unit * 0.50
    elif(unit<=150):
        El = (50 * 0.50) + (unit - 50) * 0.75
    elif(unit<=250):
        El = (50 * 0.50) + (100 * 0.75) + (unit - 150) * 1.20
    else:
        El = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + (unit - 250) * 1.50

    bill = El * 0.20 
    total_bill = bill + El
    print("Total Bill:", round(total_bill, 2))
else:
    print("Invalid input")
