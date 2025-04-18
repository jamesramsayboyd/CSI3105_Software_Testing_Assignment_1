# Variables
customer_id = 1234
loan_type = "H"
loan_amount = 200.0
monthly_interest_rate = 0.03
late_penalty = 100.0


# customer ID must be 4-8 characters long, no other criteria
def validate_customer_id(x):
    if 999 < x <= 99999999:
        return True
    else:
        print("invalid customer id")
        return False


# loanType must be "H", "C" or "P"
def validate_loan_type(x):
    if x == "H" or x == "C" or x == "P":
        return True
    else:
        print("invalid loan type")
        return False


# Must be positive double between 100.000 and 800,000.00
def validate_loan_amount(x):
    if 100.00 <= x <= 800000.00:
        return True
    else:
        print("invalid loan amount")
        return False


# Must be positive double between 0.01 and 0.045
def validate_monthly_interest_rate(x):
    if 0.01 <= x <= 0.045:
        return True
    else:
        print("invalid monthly interest rate")
        return False


# Must be 0 or 100
def validate_late_penalty(x):
    if x == 0.0 or x == 100.0:
        return True
    else:
        print("invalid late penalty")
        return False


# Throws error unless all inputs are valid
def validate_input():
    if validate_customer_id(customer_id):
        if validate_loan_type(loan_type):
            if validate_loan_amount(loan_amount):
                if validate_monthly_interest_rate(monthly_interest_rate):
                    if validate_late_penalty(late_penalty):
                        return True
    else:
        return False


def calculate_monthly_interest_repayment():
    monthly_interest_repayment = loan_amount * monthly_interest_rate + late_penalty
    return monthly_interest_repayment


def print_variables():
    print(str(customer_id) + ", " + str(loan_type) + ", " + str(loan_amount), ", " + str(monthly_interest_rate) + ", " + str(late_penalty) + ", monthly interest repayment is " + str(calculate_monthly_interest_repayment()))


def main():
    if validate_input():
        print_variables()
    else:
        print("Customer ID invalid")


main()
