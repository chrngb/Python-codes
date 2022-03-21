# Rock Paper Scissors game
while True:
    import random

    print("Rock Paper Scissors game")

    print('Enter your choice. Type "1" for Rock, "2" for Paper, "3" or Scissors')
    choices = ["1", "2", "3"]
    options = ["Rock", "Paper", "Scissors"]

    while True:
        user_input = input("-> ")
        if user_input not in choices:
            print(
                'Invalid input. Please type "1" or Rock, "2" for Paper, "3" or Scissors')
        else:
            break

    user_choice = int(user_input)
    print("You chose:", options[user_choice-1])

    cpu_choice = random.randint(1, 3)
    print("CPU chose:", options[cpu_choice-1])

    if user_choice == cpu_choice:
        print("Its a draw.")
    elif (user_choice == 1 and cpu_choice == 3) or\
        (user_choice == 2 and cpu_choice == 1) or\
            (user_choice == 3 and cpu_choice == 2):
        print("You Win!")
    else:
        print("You Lose!")

    again = input("Play again? (y/n) -> ")
    if again != "y":
        break
