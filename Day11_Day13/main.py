expenses = [2200,2350,2600,2130,2190]
months = ["January", "February","March",]

print(f"You spent {expenses[1]-expenses[0]} in February more than you did in January")

print(f"You spent {sum(expenses[0:3])} in the first quarter ")

print("Did I spend in any given month?", 2000 in expenses)

expenses.append(1980)
print(expenses)

expenses[3] = expenses[3] - 200
print(expenses)