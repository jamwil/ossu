def part_b(yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise):
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
	    # Take our raise if we're on a 6-month anniversary
	    if months % 6 == 0:
	        yearly_salary *= 1 + semi_annual_raise
	        monthly_salary = yearly_salary / 12
	
	return months