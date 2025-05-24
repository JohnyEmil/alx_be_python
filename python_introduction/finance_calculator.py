monthly_income = float(input("Enter your monthly income:"))
monthly_expenses = float(input("Enter your total monthly expenses:"))

monthly_saving = monthly_income - monthly_expenses

annual_rate = 0.05
projected_saving = (monthly_saving * 12) + (monthly_saving * 12 * annual_rate)

print(f"Your monthly savings are ${int(monthly_saving)} \nProjected savings after one year, with interest, is: ${int(projected_saving)}.")