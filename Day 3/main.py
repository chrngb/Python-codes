# Treasure Hunt

print("Welcome to treasure island.")
print("Can you find the treasure?")

game_over = False
victory = False

print("You're at a cross road. Where do you want to go \"left\" or \"right\"")
choice1 = input("-> ").lower()

if choice1 == "left":
    print('You\'ve arrived at a lake. There is an island at the middle of lake. \nDo you want to "wait" for a boat or "swim"?')
    choice2 = input("-> ").lower()

    if choice2 == "wait":
        print('You\'ve now arrived at the island. You find a house with 3 doors of colours' ' "red", "blue" and "green". Which door you want to choose?')
        choice3 = input("-> ").lower()

        if choice3 == "red":
            print("You entered a room full of fire. You're dead.")
            game_over = True

        elif choice3 == "blue":
            print("You entered a room full of beasts. You're dead.")
            game_over = True

        elif choice3 == "green":
            print("Congrats!!! You found the treasure.")
            victory = True

        else:
            print("You chose a door that doesn't exist.")
            game_over = True

    else:
        print("You are attacked by angry trouts. You're dead.")
        game_over = True

else:
    print("You fell into a deep hole. You're dead.")
    game_over = True

if game_over:
    print("Game Over")
elif victory:
    print("Victory")
