#create a program that asks for user for their name and age
name = input('What is your name? \n')
age = int(input('How old are you? \n'))
current_year = int(input('Type the current year: \n'))

life_span = 100 
tmp_age = life_span - age
centinnial_age = tmp_age + age

#current_date = datetime.datetime()
centinnial_year = current_year + tmp_age

#Print a message to them that tells them when they will turn 100.
if centinnial_age == 100:
    print(f"{name} you will turn 100 in {centinnial_year}.")