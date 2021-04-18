def account_number_validation(account_number):

    if account_number :
      
        try:
            int(account_number)

            if len(str(account_number)) == 10:
            
                return True
            else:

                return False

        except ValueError:
       
            return False
        except TypeError:
            
            return False

    return False

# def password_validation(pin):

#     if password:

#         try:
#             int(password)

#             if len(str(password)) == 4:
#                 return True

#         except ValueError:
#             return False
#         except TypeError:
#             return False

#     return False