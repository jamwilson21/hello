#ask the user for a number
user_input = int(input('Please enter a number: \n'))

#depending on whether the number is even or odd
if(user_input % 4 == 0):
    print(f'{user_input} is divisible by 4.')
    
elif(user_input % 2 and user_input != 0):
    print('This is an odd number.')   

elif(user_input % 2 == 0):
    print('This is an even number.')

num = int(input('Please enter a number: \n'))
check = int(input('Please enter another number. \n'))

#check divides evenly into num
if(check % num == 0 ):
   print(f'{check} divides evenly into {num}.')
else:
    print(f'{check} did not divide evenly into {num}.')  

#print an appropriate message to the user