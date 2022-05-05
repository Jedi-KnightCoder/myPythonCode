#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? " ))
people = int(input("How many people to split the bill? "))

# bill_total = total_bill * (1 + (tip / 100))
bill_total = tip /100 * total_bill + total_bill
#tip_totalbill = total_bill + tip
# split_bill = tip_totalbill // people_to_split_bill                    
#split_bill = round((bill_total / people), 2)
split_bill = "{:.2f}".format(bill_total / people)
print(f"Each person should pay: ${split_bill}" )

