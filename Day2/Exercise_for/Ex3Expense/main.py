expense_list = [2340, 2500, 2100, 3100, 2980]
month_list = ["January","February","March","April","May"]

expense = int(input("Enter the expense amount\n"))

for i in range(len(expense_list)):
    if expense == expense_list[i]:
        month = i
    else: break


if expense in expense_list:
    print(f'you spent {expense} in {month_list[month]}')
else:
    print(f'You did not spend {expense} in any month')