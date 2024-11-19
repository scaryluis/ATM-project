# First define the given balance in the global scope outside
balance = 1000

# Create function for depositing
def deposit_money():
    global balance
    amount = int(input("Enter amount to deposit: "))
    balance += amount #Add inputted amount to the total balance
    print("Deposit complete, your new balance is:",balance)

#Create function to be able to withdraw money
def withdraw_money():
    global balance #Again pull the balance from the global scope
    amount= int(input("Enter amount to withdraw: "))
    if amount > balance: #create "if" statement to see if the amount inputted exceeds balance
        print("You do not have enough funds.") #Create error message
    else:
        balance -= amount
        print("Withdrawal complete. Your new balance is: ",balance) #Create success method and show new balance

#Create function to check the balance
def check_balance():
    print("Your balance is:",balance) #Create simple print string that displays the users balance

#Create exit atm function for the user to exit the atm
def exit_atm():
    print("Goodbye!") #Create a goodbye message
    exit() #Call this to stop executing the function

#Create an ATM menu function for the user to see their options and input their choice
def atm_menu():
    while True: #Create a while loop that displays the options
        print("Welcome to the ATM!")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")

        #Create an exception where the program expects a user might input a number that is not an option
        try:
            choice = int(input("Choose an input: ")) #Call the functions based on the input
            if choice == 1:
                deposit_money()
            elif choice == 2:
                withdraw_money()
            elif choice == 3:
                check_balance()
            elif choice == 4:
                exit_atm()
            else:
                print("Invalid option, choose from 1-4.") #print this incase a user inputs a number that is not an option
        except ValueError:
            print("Invalid input, please enter a Number.") #Create the except incase the user inputs
                                                           #something other than a number

#Call the ATM menu to show the user the options to begin
atm_menu()
