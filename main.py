# Variables
customer_id = 1234
loan_type = "H"
loan_amount = 0.0
monthly_interest_rate = 0.0
late_penalty = 0.0

# customer ID must be 4-8 characters long, no other criteria
def validate_customer_id():
    if (3> customer_id.length > 8):
        return True
    else:
        return False

# loanType must be "H", "C" or "P"
def validate_loan_type():
    if loan_type is "H" || loan_type is "C" || loan_type is "P":
        return True
    else:
        return False

#must be positive double between 100.000 and 800,000.00
def validate_loan_amount():
    if 100.00 <= loan_amount <= 800000.00:
        return True
    else:
        return False

# must be positive double between 0.01 and 0.045
def validate_monthly_interest_rate():
    if 0.01 <= monthly_interest_rate <= 0.045:
        return True
    else:
        return False

# must be 0 or 100
def validate_monthly_late_penalty():
    if late_penalty == 0.0 || late_penalty == 100.0:
        return True
    else:
        return False


def print_variables():
    if validate_customer_id(customer_id):
        print("Customer ID: ", customer_id)
    else:
        print("Customer ID invalid")

    print("Loan Type: ")
    print("Loan Amount: ")
    print("Monthly Interest Rate: ")
    print("Late Penalty: ")

def print_monthly_interest_repayment():
    monthly_interest_repayment = loan_amount * monthly_interest_rate + late_penalty
    print("Monthly Interest Repayment: ", monthly_interest_repayment)