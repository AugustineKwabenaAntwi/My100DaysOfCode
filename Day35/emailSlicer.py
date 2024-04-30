def program():
    print("This is an email slicer\n\n")

    email = input("Enter the email address here: ")
    username, domain = email.split("@")
    
    domain, extension = domain.split(".")

    print(f"Username:{username}\n")
    print(f"Domain:{domain}\n")
    print(f"Extension:{extension}\n")

program()
