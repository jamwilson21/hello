def animal_legs(chicken, cow, deer):
    print('How many animal legs? \n')
    chicken_legs = 2
    cow_legs = 4
    deer_legs = 4

    total_chicken_legs = chicken_legs * chicken
    total_cow_legs = cow_legs * cow
    total_deer_legs = deer_legs * deer

    animal_sum = total_chicken_legs + total_cow_legs + total_deer_legs
    return animal_sum

print(animal_legs(8, 12, 4))
