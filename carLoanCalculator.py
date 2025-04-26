# Constants
INTEREST_RATE = 0.05  

# Functions
def get_user_info():
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()
    return first_name, last_name

def get_loan_info():
    loan_amount = float(input("Enter the loan amount ($): "))
    down_payment = float(input("Enter your down payment ($): "))
    return loan_amount, down_payment

def choose_term():
    terms = [84, 72, 60, 48]
    print("\nAvailable terms in months:")
    for index, term in enumerate(terms, start=1):
        print(f"{index}. {term} months")

    choice = int(input("Select a term (1-4): "))
    if 1 <= choice <= 4:
        return terms[choice - 1]
    else:
        print("Invalid choice. Defaulting to 60 months.")
        return 60

def calculate_monthly_payment(loan_amount, down_payment, months):
    principal = loan_amount - down_payment
    total_amount = principal * (1 + INTEREST_RATE)
    monthly_payment = total_amount / months
    return monthly_payment

def display_summary(full_name, monthly_payment, months):
    print("\n==== Loan Summary ====")
    print(f"Name: {full_name}")
    print(f"Monthly Payment for {months} months: ${monthly_payment:.2f}")
    print("======================")


def main():
    first_name, last_name = get_user_info()
    loan_amount, down_payment = get_loan_info()
    months = choose_term()
    monthly_payment = calculate_monthly_payment(loan_amount, down_payment, months)
    full_name = f"{first_name} {last_name}"
    display_summary(full_name, monthly_payment, months)


if __name__ == "__main__":
    main()