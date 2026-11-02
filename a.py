def total_calc(bill_amount, tip_perc):

    total = bill_amount + bill_amount*tip_perc/100
    total = round(total, 0)
    print("Please pay $",total,sep="")

total_calc(150,20)