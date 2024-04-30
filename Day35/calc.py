def add(a,b):
    answer = a+b
    print(f" {a} + {b} = {answer}")

def sub(a,b):
    answer = a-b
    print(f" {a} - {b} = {answer}")

def mult(a,b):
    answer = a*b
    print(f" {a} x {b} = {answer}")
    
def div(a,b):
    answer = a/b
    print(f" {a} / {b} = {answer}")

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")


    choice = input("Enter the operation you want ").capitalize()

    if choice =="A":
        print('addition');
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        add(a,b)
    elif choice =="B":
        print('subtraction');
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        sub(a,b)
    elif choice =="C":
        print('multiplication');
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        mult(a,b)
    elif choice =="D":
        print('division');
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        div(a,b)
    elif choice =="E":print('Exit the program');quit()
    