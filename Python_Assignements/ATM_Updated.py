#generate a date when a customer logs into an account 
import datetime
#generate a random account number for a new customer
import random
#all the input of a password
import getpass
current_Date = datetime.datetime.today()


# this database should store existing and capture new customer data; dictionary
database = {}


# welcome customers
def welcome():
    print("*********************Welcome to Python Bank*********************")
    customer = int(input("Are you a new or existing customer? (1) New or (2) Existing \n"))
    
    if customer == 1:
        print("Hi, let's create you an account.")
        register()           

    #elif customer == 2:
        print("Welcome back, please login: \n")
        login()
    
    else:
        print("You have selected an invalid option.")
        welcome()

def login():      
    print("********* Login ***********")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    for accountNumber,userPassword in database.items():
        if accountNumber == accountNumberFromUser and userPassword[3] == password:
                bankOperation(userPassword)           
            #bankOperation(userPassword)

#register the new customer  
def register():
    print("****** Register *******")
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    pin = input("Type four numbers: \n")
   
    account_number = generationAccountNumber()
    
    database[account_number] = [ email, first_name, last_name, pin ]
    
    
    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % account_number)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")
    login()
     

# new and existing customers should be able to perform banking operations
def bankOperation(user):
    print("Welcome %s  %s " % (user[1], user[2]))
    print('Current Date: ' + str(current_Date))
    print('These are the available options:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Compliant')

    selectOption = int(input('Please select an option: \n'))
    current_balance = 1000
    withdraw_amount = 500
    
    if selectOption == 1:
        print('You selected %d' % selectOption)
        withdraw = int((input("How much would you like to withdraw?\n")))   
        withdraw_amount = withdraw 
        current_balance = current_balance - withdraw_amount
        print("Please take your cash. Have a great day.")
        logout()
        
    elif selectOption == 2:
        print('You selected %d' % selectOption) 
        deposit = int((input("How much would you like to deposit?\n")))
        deposit_amount = deposit
        current_balance = deposit_amount + withdraw_amount
        print("Your current balance is %s. Haveb a great day" % current_balance)
        logout()
       
       
    elif selectOption == 3:
        print('You selected %d' % selectOption) 
        issue = (input("What issue would you like to report?\n"))
        print(f"Your issue is : {issue}.")
        print("Thank you for reporting your the above issue. A Customer Service Representative will contact you soon by email.")
        exit()
    

    else:
        print('Invalid Option selected, please try again.')
        bankOperation()

    login()
def generationAccountNumber():
    
    return random.randrange(1111111111,9999999999)

def logout():
    print("Thanks for being a customer. Have a great day!")
    

#Only need to run welcome
welcome()
