#   create
#   update record
#   read record
#   delete record
#   find record
#   CRUD

import os
import validation

user_db_path = "Python_Assignements/data/user_record/"
user_db_auth_path = "Python_Assignements/data/auth_session/"

def create(account_number, first_name, last_name, email, password, balance):
    user_details = first_name + "," + last_name + "," + email + "," + password + "," + str(balance)

    if does_account_number_exist(account_number):
        return False

    if does_email_exist(email):
        print("User already exist")

    complete_state = False

    try:
        f = open(user_db_path + str(account_number) + ".txt", "x")
    except FileExistsError:

        does_file_contain_data = read(user_db_path + str(account_number) + ".txt")
        if not does_file_contain_data:
            delete(account_number)
    else:

        f.write(str(user_details))
        f.close()
        complete_state = True

    finally:
        return complete_state


def read(account_number):
    is_valid_account_number = validation.account_number_validation(account_number)
    if not is_valid_account_number:
        return False
    try:
        f = open(user_db_path + str(account_number) + ".txt", "r")

    except FileNotFoundError:
        print("User not found")
    except FileExistsError:

        print("User already exist")

    else:
        return f.readline()


# read the contents of the file to locate the account number

def update(account_number, user):
    try:
        f = open(user_db_path + str(account_number) + ".txt", "w")
        f.write(','.join(user))
    except FileNotFoundError:
        print("User not found")
    except FileExistsError:

        print("Account already exists")

    except TypeError:
        print("Invalid account number format")
    else:
        f.close()
        return True
    return False

def delete(account_number):
    if os.path.exists(user_db_path + str(account_number) + '.txt'):
        os.remove(user_db_path + str(account_number) + '.txt')
        is_delete_successful = True
    else:
        print("Account doesn't exist.")
        is_delete_successful = False
    return is_delete_successful


def does_email_exist(email):
    all_users = os.listdir(user_db_path)

    for user in all_users:
        user_list = str.split((user), ',')
        if email in user_list:
            return True
    return False


def does_account_number_exist(account_number):
    all_users = os.listdir(user_db_path)

    for user in all_users:
        if user == str(account_number) + ".txt":
            return True
    return False


def authenticated_user(account_number, password):
    if does_account_number_exist(account_number):
        user = str.split((account_number), ',')
        if password == user[3]:
            return user
    return False

def start_auth(user):
    # the start of login session.

    try:
        f = open(user_db_auth_path + str(user) + ".txt", 'x')
        f.write(str((user)))
        f.close()
    except FileExistsError:  # If file exists, user is logged on.
        return "Authentication started"
        exit()


def end_auth(user):
    if os.path.exists(user_db_auth_path + str(user) + '.txt'):
        os.remove(user_db_path + str(user) + '.txt')
        is_delete_successful = True
    else:
        print("Account doesn't exist.")
        is_delete_successful = False
    return is_delete_successful


