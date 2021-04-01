import datetime
 
name = input("What is your username? \n")
allowedUsers = ['Seyi', 'Mike', 'Love']
allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove']
Current_Date = datetime.datetime.today()

if(name in allowedUsers):
    password = input("Your password? \n")
    userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):
        print('Welcome %s' % name)
        print('Current Date: ' + str(Current_Date))
        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Compliant')

        selectOption = int(input('Please select an option:'))
        current_balance = 1000
        withdraw_amount = 500

        if(selectOption == 1):
            print('You selected %s' % selectOption)
            withdraw = int((input("How much would you like to withdraw?\n")))
            withdraw_amount = withdraw 
            current_balance = current_balance - withdraw_amount
            print("Then take out cash.")
            print('These are the available options:')
            print('1. Withdrawal')
            print('2. Cash Deposit')
            print('3. Compliant')

            selectOption = int(input('Please select an option:'))
    
        elif(selectOption == 2):
            print('You selected %s' % selectOption) 
            deposit = int((input("How much would you like to deposit?\n")))
            deposit_amount = deposit
            current_balance = deposit_amount + withdraw_amount
            print("Your current balance is %s." % current_balance)
            print('These are the available options:')
            print('1. Withdrawal')
            print('2. Cash Deposit')
            print('3. Compliant')

            selectOption = int(input('Please select an option:'))

        elif(selectOption == 3):
            print('You selected %s' % selectOption) 
            issue = (input("What issue would you like to report?\n"))
            issue_stored = issue
            print("Thank you for contacting us.")
            print('These are the available options:')
            print('1. Withdrawal')
            print('2. Cash Deposit')
            print('3. Compliant')

            selectOption = int(input('Please select an option:'))

        else:
            print('Invalid Option selected, please try again.')
    
    else:
        print('Password Incorrect, please try again')

else: 
    print('Name not found, please try again')