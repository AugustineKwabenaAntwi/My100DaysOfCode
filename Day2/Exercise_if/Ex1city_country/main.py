india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

query = input("Enter the name of a city ")

if query in india:
    print("%s is in India" %query)
elif query in pakistan:
    print("%s is in Pakistan" %query)
elif query in bangladesh:
    print("%s is in Bangladesh" %query)
else: print("I dont have your input in my database")
