import hangman_art as art
import hangman_words as words
import random


def get_guess():
    while True:
        g = input("Guess a letter: ").lower()
        if g in guessed_letter_list:
            print(f"You have already guessed the letter \"{g}\".")

        elif g not in letter_list:
            print("The guess has to be a single letter. Please try again.")

        else:
            return g


chosen_word = list(random.choice(words.word_list))

letter_list = list("abcdefghijklmnopqrstuvwxyz")

guessed_letter_list = []

ri = random.randrange(len(chosen_word))
hint = chosen_word[ri]

display = []

for i in range(len(chosen_word)):
    display.append("_")

display[ri] = hint
guessed_letter_list.append(hint)

game_over = False
is_winner = False

lives = len(art.stages) - 1

print(art.logo)
print("The word is: ")
print(" ".join(display))

while not game_over:
    guess = get_guess()
    guessed_letter_list.append(guess)

    good_guess = False

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
            good_guess = True

    if good_guess:
        if display.count("_") == 0:
            is_winner = True
            game_over = True

    else:
        print(f"The letter \"{guess}\" is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_over = True

    print(" ".join(display))
    print(art.stages[lives])

print(f"Pssst, the solution is \"{''.join(chosen_word)}\".")
