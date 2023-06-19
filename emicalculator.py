def calculate_emi(principal, interest_rate, tenure):
    monthly_interest_rate = interest_rate / 12 / 100
    emi = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** tenure) / ((1 + monthly_interest_rate) ** tenure - 1)
    return emi

def main():
    principal = float(input("Enter the loan amount: "))
    interest_rate = float(input("Enter the annual interest rate: "))
    tenure = int(input("Enter the loan tenure in months: "))

    emi = calculate_emi(principal, interest_rate, tenure)
    total_amount = emi * tenure

    print("Loan Amount: $", principal)
    print("Interest Rate: ", interest_rate, "%")
    print("Loan Tenure: ", tenure, " months")
    print("Monthly EMI: $", round(emi, 2))
    print("Total Payable Amount: $", round(total_amount, 2))

if __name__ == '__main__':
    main()
