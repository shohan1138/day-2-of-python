Height=input("enter your height in mitre:")
Weight=input("enter your weight in kg:")


BMI=int(Weight)/float(Height)**2
print(BMI)
bmi_as_int=int(BMI)
bmi_as_round=round(BMI)
print(bmi_as_int)
print(bmi_as_round)

#f-String
print(f"your height is {Height},your weight is {Weight}, and yout bmi rating is {bmi_as_round}")

