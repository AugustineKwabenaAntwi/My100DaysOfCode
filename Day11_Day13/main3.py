max_number = int(input("Please input your max number here: "))

for number in range(1,max_number +1 ):
    if number%2 == 0:
        continue
    else:print(number)