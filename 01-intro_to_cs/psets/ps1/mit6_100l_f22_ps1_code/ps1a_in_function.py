def part_a(yearly_salary, portion_saved, cost_of_dream_home):
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
	    monthly_return = amount_saved * (r / 12)
	    months += 1
	    amount_saved += (monthly_salary * portion_saved) + monthly_return
	return months