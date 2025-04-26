# ATM Final Project
# Author: Tulio Salvatierra
# Date: 4/23/2025


INTEREST_RATE = 0.01  


starting_balance = 1000.00  


USER = "tulio"
PASSWORD = "1234"


def login():
    print("=== Welcome to ATM System ===")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == USER and password == PASSWORD:
        print("Login successful!\n")
        return True
    else:
        print("Incorrect username or password. Exiting...")
        return False

def show_menu():
    print("\n--- ATM Menu ---")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. View Interest Accrued")
    print("4. Exit")

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount < 0:
        print("Negative entries are not allowed.")
        return balance
    elif amount > balance:
        print("Insufficient funds.")
        return balance
    else:
        balance -= amount
        print(f"${amount:.2f} withdrawn successfully.")
        return balance

def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    if amount < 0:
        print("Negative entries are not allowed.")
        return balance
    else:
        balance += amount
        print(f"${amount:.2f} deposited successfully.")
        return balance

def calculate_interest(balance):
    interest = balance * INTEREST_RATE
    print(f"Interest accrued so far: ${interest:.2f}")
    return interest

def save_to_file(full_balance):
    with open("atm_transactions.txt", "a") as file:
        file.write(f"Final balance: ${full_balance:.2f}\n")


def main():
    balance = starting_balance

    if not login():
        return  

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            balance = withdraw(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            calculate_interest(balance)
        elif choice == "4":
            print(f"Exiting. Final balance: ${balance:.2f}")
            save_to_file(balance) 
            break
        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()