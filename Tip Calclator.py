# Tip Calculator
print("Welcome to your tip calculator")
bill = input("Please enter the amount of the bill £")
split = input("How many people want to split the bill? ")
bill_per = input("Please enter the amount you would like to tip, 10%, 12% or 15%? ")

new_bill_per = float(bill) * float(bill_per) / 100
new_bill = float(new_bill_per) + float(bill)
split_a = float(split)
full_new_bill = float(new_bill) / split_a

print(f"You each have to pay {full_new_bill:.2f}")

# Alternative
# This prevents the above, having to convert the var into int or float individually
# bill = float(input("Please enter the amount of the bill £"))
# tip = int(input("How would you like to tip? Maybe 10, 12 or 15 without the %"))
# split = int(input("How many people will split the bill? "))
# var = {:.2f}.format(var) Rather than placing it within the final print
# print (f"Each person should pay £{var})