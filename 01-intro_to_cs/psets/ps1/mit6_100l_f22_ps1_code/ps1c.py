## 6.100A PSet 1: Part C
## Name: James Williams
## Time Spent: 45 minutes
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
cost_of_dream_home = 800_000
portion_down_payment = 0.25
total_down_payment = cost_of_dream_home * portion_down_payment
months = 36
epsilon = 100


##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
def amount_saved(guess: float) -> float:
    return initial_deposit * ((1 + (guess / 12)) ** months)

low = 0.0
high = 1.0
r = 0.5

steps = 1
while abs(amount_saved(r) - total_down_payment) >= epsilon:
    if amount_saved(r) < total_down_payment:
        low = r
    else:
        high = r

    r = (high + low) / 2.0

    if r < 0.0001:
        r = 0.0
        break

    if 1.0 - r < 0.0001:
        r = None
        break

    steps += 1

print(f"Best rate of return: {r} in {steps} steps")

