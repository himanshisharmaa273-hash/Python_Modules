name = input("Enter your name:")
monthly_income = int(input("Enter monthly income:"))
rent = int(input("Enter rent:"))
food_expenses = int(input("Enter food expenses:"))
travel_expenses = int(input("Enter travel expenses:"))
entertainment_expenses = int(input("Enter entertainment expenses:"))
other_expenses = int(input("Enter other expenses:"))

print("Name:",name)
print("Monthly Income:",monthly_income)

total_expenses = rent+food_expenses+travel_expenses+entertainment_expenses+other_expenses
print("Total Expenses:", total_expenses)

remaining_money = monthly_income-total_expenses
print("Remaining Money:", remaining_money)

saving_percentage= (remaining_money/monthly_income)*100
print(f"Savings Percentage:{saving_percentage}%")

daily_average = total_expenses/30
print(f"Daily Average spending is {daily_average}")

weekly_average = total_expenses/4
print(f"Weekly Average spendin is {weekly_average}")



