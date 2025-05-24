incomes = input("Enter your monthly income:")
expenses = input("Enter your total monthly expenses:")

monthly_saving = float(incomes) - float(expenses)

annual_rate = 0.05
projected_saving = (monthly_saving * 12) + (monthly_saving * 12 * annual_rate)

print(f"Your monthly savings are ${monthly_saving} \nProjected savings after one year, with interest, is: ${projected_saving}.")