#create a list that takes in vaules
children_age = input("Type your children ages seperated by a space: \n")
temp = children_age.split()

# change string to int
for numbers in range(len(temp)):
    temp[numbers] = int(temp[numbers])

#write a program that prints all variables less than 5
for ages in temp[numbers]:
    if(ages < 10):
        print(ages)