monthly_income = int(input("Enter your monthly income:"))
total_monthly_expenses = int(input("Enter your total monthly expenses:"))

monthly_savings = monthly_income - total_monthly_expenses

currency = '${:}'.format(monthly_savings)

print("Your monthly savings are",currency)

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

projected_savings_currency = '${:}'.format(projected_savings)

print("Projected savings after one year, with interest, is:", projected_savings_currency)

