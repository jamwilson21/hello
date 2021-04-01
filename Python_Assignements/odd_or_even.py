#ask the user for a number
user_input = int(input('Please enter a number: \n'))

#depending on whether the number is even or odd
if(user_input / 2 ):
    print('This is an even number.')
    
elif(user_input % 2 and user_input != 0):
    print('This is an odd number.')   
#print an appropriate message to the user