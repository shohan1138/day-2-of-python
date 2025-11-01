Age=input("enter your current age: ")
age_as_int=int(Age)

year_remaining= 90-age_as_int
months_remaining= year_remaining*12
weeks_remaining= year_remaining*52
days_remaining= year_remaining*365

# print(months_remaining)

print(f"you have {months_remaining} months or {weeks_remaining} weeks or {days_remaining} days remain to reach 90 ")
