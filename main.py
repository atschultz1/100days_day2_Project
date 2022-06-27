#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator")

total_bill = input("What was the total bill?")
total_bill_as_float = float(total_bill)

tip_percent = input("What percentage tip would you like to give? 10, 12, or 15?")
tip_percent_as_int = int(tip_percent)

total_tip = total_bill_as_float * tip_percent_as_int / 100

people = input("How man people to split the bill?")
people_as_int = int(people)

total_with_tip = total_bill_as_float + total_tip 
total_per_person = total_with_tip / people_as_int
total_per_person_as_float = float(total_per_person)

print(f"Each person should pay: ${round(total_per_person_as_float, 2)}.")

#notes to self:
#it seems like a turning a lot of variables into new variables of different data types
#return to this later and see if you can shrink it
#Jon is a big ol' bitch.