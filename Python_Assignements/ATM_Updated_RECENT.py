#generate a date when a customer logs into an account
import datetime

#   generate a random account number for a new customer

import random
#   all the input of a password

from getpass import getpass

current_Date = datetime.datetime.today()

import database

import validation


#  the database should store existing and capture new customer data; dictionary
account_number = ""
email = ""
first_name = ""
last_name = ""
password = ""
balance = 0


# welcome customers
def welcome():
    print("*********************Welcome to Python Bank*********************")
    customer = int(input("Are you a new or existing customer? (1) New or (2) Existing \n"))

    if customer == 1:
        print("Hi, let's create you an account.")
        register()

    elif customer == 2:
        print("Welcome back, please login: \n")
        login()

    else:
        print("You have selected an invalid option.")
        welcome()

def login():
    print("********* Login ***********")

    account_number_from_user = input("What is your account number?\n")
    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("What is your password?:\n")
        user = database.authenticated_user(account_number_from_user, password)
        user_auth_session = database.auth_login(str(account_number),first_name, last_name, email, password, str(balance))
        
        if user:
            bank_operation(user, account_number_from_user)
        elif user_auth_session:
            print("===== Session has began =====")
        print("Invalid account or pin")
        login()
    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers.")
        welcome()

def register():
    print("****** Register *******")
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Please type your password: \n")
    balance = 0

    account_number = generation_account_number()
    is_user_created = database.create(str(account_number),first_name, last_name, email, password, str(balance))

    if is_user_created:
        print("Your Account Has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("Something went wrong, please try again.")
        register()


# new and existing customers should be able to perform banking operations
def bank_operation(user, account_number):

    print("Welcome %s  %s " % (user[0], user[1]))
    print('Current Date: ' + str(current_Date))
    print('These are the available options:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Compliant')

    select_option = int(input('Please select an option: \n'))

    if select_option == 1:
        print('You selected %d' % select_option)
        withdraw(user, account_number)

    elif select_option == 2:
        print('You selected %d' % select_option)
        deposit(user, account_number)

    elif select_option == 3:
        print('You selected %d' % select_option)
        issue = (input("What issue would you like to report?\n"))
        print(f"Your issue is : {issue}.")
        print("Thank you for reporting your the above issue. A Customer Service Representative will contact you soon by email.")
        exit()


    else:
        print('Invalid Option selected, please try again.')
        bank_operation(user, account_number)

    welcome()

def withdraw(user, account_number):
    get_user_balance = int(user[4])
    print("This is your current balance %d " % get_user_balance)
    amount_to_withdraw = int((input("How much would you like to withdraw?\n")))
    current_user_balance = get_user_balance - amount_to_withdraw
    if amount_to_withdraw > get_user_balance:
        print("You do not have enough funds to withdraw at this time.")
    else:
        user[4] = str(current_user_balance)
        database.update(account_number, user)
    print("Your current balance is %s. Have a great day." % current_user_balance)
    logout()
    exit()

def deposit(user, account_number):
    get_user_balance = int(user[4])
    print("This is your current balance %d " % get_user_balance)
    amount_to_deposit = int((input("How much would you like to deposit?\n")))
    current_user_balance = get_user_balance + amount_to_deposit
    user[4] = str(current_user_balance)
    print("Your current balance is %s. Have a great day." % current_user_balance)
    database.update(account_number, user)
    exit()

def generation_account_number():

    return random.randrange(1111111111, 9999999999)

def logout():
    print("Thanks for being a customer.")

welcome()
