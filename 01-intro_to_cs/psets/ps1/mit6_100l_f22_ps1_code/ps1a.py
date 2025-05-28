## 6.100A PSet 1: Part A
## Name: James Williams
## Time Spent: 30 minutes
## Collaborators: -


##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Yearly salary: "))
portion_saved = float(input("Portion saved: "))
cost_of_dream_home = float(input("Home value: "))


#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
down_payment = cost_of_dream_home * portion_down_payment
monthly_salary = yearly_salary / 12
r = 0.05


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ##
###############################################################################################
amount_saved = 0.0
months = 0
while amount_saved < down_payment:
    # Calculate the interest based on the balance at the start of the month
    monthly_return = amount_saved * (r / 12)
    # Add the monthly savings + the monthly return to the running balance
    amount_saved += (monthly_salary * portion_saved) + monthly_return
    months += 1
