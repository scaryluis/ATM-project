# First define the balance in the global scope
balance = 1000

# Create function for depositing
def deposit_money():
    global balance
    amount = int(input("Enter amount to deposit: "))
    balance += amount
    print("Deposit complete, your new balance is:",balance)

def withdraw_money():
    global balance
    amount= int(input("Enter amount to withdraw: "))
    if amount > balance:
        print("You do not have enough funds.")
    else:
        balance -= amount
        print("Withdrawal complete. Your new balance is: ",balance)

def check_balance():
    print("Your balance is:",balance)

def exit_atm():
    print("Goodbye!")
    exit()

def atm_menu():
    while True:
        print("Welcome to the ATM!")
        print("1. Deposit Money")
        print("2. Withdrawal Money")
        print("3. Check balance")
        print("4. Exit")

        try:
            choice = int(input("Choose and input: "))
            if choice == 1:
                deposit_money()
            elif choice == 2:
                withdraw_money()
            elif choice == 3:
                check_balance()
            elif choice == 4:
                exit_atm()
            else:
                print("Invalid option, choose from 1-4.")
        except ValueError:
            print("Invalid input, please enter a number.")

atm_menu()
