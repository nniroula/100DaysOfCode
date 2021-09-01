#!/Users/nabinniroula/anaconda3/bin/python

""" generate a random number, ask user to guess, and keep track of number of times user takes to make correct guess"""

import random

def guess_a_number_game():
    random_number = random.randint(0, 10)
    # print(random_number)
    counter = 0
    # Ask a user to make a guess
    user_input = int(input("Enter a number between 0 and 10; 10 exclusive: "))
    counter += 1
    if user_input == random_number:
        counter = counter

    while not user_input == random_number:
        if user_input > random_number:
            print("Guess a smaller number.")
            user_input = int(input("Enter a number between 0 and 10; 10 exclusive: "))
            counter += 1
        elif user_input < random_number:
            print("Guess a bigger number.")
            user_input = int(input("Enter a number between 0 and 10; 10 exclusive: "))
            counter += 1
       
    return f"Attempts = {counter} times."

print(guess_a_number_game())
