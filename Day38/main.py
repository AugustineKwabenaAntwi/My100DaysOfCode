def main():
    print("Loan Monthly payment calculator \n\n")

    principal = float(input("The Loan Amount: "))

    apr = float(input("The annual interest rate: "))

    years = int(input("The number of years"))

    monthly_interest_rate = apr/1200
    number_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate/(1-(1+monthly_interest_rate)**(-number_of_months))

    print("Monthly payment is %.2f "% monthly_payment)

main()