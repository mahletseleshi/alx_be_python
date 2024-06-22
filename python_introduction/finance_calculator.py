income = int(input("Enter your monthly income:  "))
expense = int(input("Enter your total monthly expenses  "))
monthly_saving = income - expense
projected_savings = monthly_saving * 12 + (monthly_saving * 12 * 0.05)

monthly_saving = income - expense


print("your monthly saving are", monthly_saving)
print("Projected savings after one year, with interest, is", projected_savings)
