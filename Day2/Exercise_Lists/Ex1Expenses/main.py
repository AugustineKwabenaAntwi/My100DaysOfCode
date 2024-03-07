expense = [2200,2350,2600,2130,2190]

#In Feb, how many dollars you spent extra compare to January?
print(expense[1]-expense[0])

#Find out your total expense in first quarter (first three months) of the year.
print(sum(expense[0:3]))

# Find out if you spent exactly 2000 dollars in any month
print("Did I spend 2000 in any month?", 2000 in expense)

# June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expense.append(1980)
print(expense)

'''You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this'''
expense[3] = expense[3]-200
print(expense)