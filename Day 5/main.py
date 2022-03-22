# Password Generator

import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password generator program")

print("How many letters do you want?")
num_letters = int(input("-> "))

print("How many  numbers do you want?")
num_numbers = int(input("-> "))

print("How many symbols do you want?")
num_symbols = int(input("-> "))

total_char = num_letters + num_numbers + num_symbols

choice = input("Do you want easy 'E' or hard password 'H' -> ")

if choice == 'e':
    password1 = ''

    for i in range(num_letters):
        password1 += random.choice(letters)

    for i in range(num_symbols):
        password1 += random.choice(symbols)

    for i in range(num_numbers):
        password1 += random.choice(numbers)

    print(f"Your easy password of {total_char} characters is:", password1)

elif choice == 'h':
    password_list = []

    for i in range(num_letters):
        password_list += random.choice(letters)

    for i in range(num_symbols):
        password_list += random.choice(symbols)

    for i in range(num_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password2 = ''

    for char in password_list:
        password2 += char

    print(f"Your hard password of {total_char} characters is:", password2)

else:
    print("Invalid Entry.")
