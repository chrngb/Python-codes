while True:
    city_name = input("Enter your birth city: ")
    if city_name.isalpha() == False:
        print("Please only enter alphabets. Try again.")
    else:
        break


while True:
    pet_name = input("Enter your pet name: ")
    if pet_name.isalpha() == False:
        print("Please only enter alphabets. Try again")
    else:
        break

print("Your band name is", city_name, pet_name)
