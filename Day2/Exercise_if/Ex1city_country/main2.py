india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

query1 = input("Enter name of first city \n")
query2 = input("Enter name of second city \n")

if query1 and query2 in india:
    print("%s and %s are in India" %(query1,query2))
elif query1 and query2 in pakistan:
    print("%s and %s are in Pakistan" %(query1,query2))
elif query1 and query2 in bangladesh:
    print("%s and %s are in Bangladesh" %(query1,query2))
else: print("I dont have your input in my database")