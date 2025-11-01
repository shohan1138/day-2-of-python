print("Welcome to the tip calculator")

Bill=float(input("What was the total Bill?:$"))

Tip=int(input("What percetage tip would you like to give?(10, 12/ 15 ):"))
people=int(input("How many people to split the bill?:"))

tip_as_percent =Tip/100
total_tip_amount = Bill*tip_as_percent
bill_with_tip=total_tip_amount +Bill

print(bill_with_tip)

each_person_pay = round(bill_with_tip/people)
print("each person will have to pay:$",each_person_pay )
