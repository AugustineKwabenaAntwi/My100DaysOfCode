user_sugar = int(input("Enter your fasting sugar level \n"))

if user_sugar>100:
    print("Your sugar level is high")
elif user_sugar<80:
    print("Your sugar level is low")
else: print("Your sugar level is normal")
