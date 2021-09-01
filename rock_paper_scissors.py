#!/Users/nabinniroula/anaconda3/bin/python
""" This is the game of the rock, paper, and scissors. It keeps track of number times a computer won and a user won.
Then displays who won in aggregation. """

import random

def rock_paper_scissors():
    random_number = random.randrange(0, 3)
    # print(random_number)
    list_of_items = ["rock", "paper", "scissors"]
    computer_generated = list_of_items[random_number]
    print(f"computer genearated, {computer_generated}.")
    tie = 0
    player_won = 0
    computer_won = 0

    while True:
        user_input = input("Enter rock, paper, or scissors, and q for quit: ")

        if user_input.lower() == 'q':
            # return f"tie = {tie}, player won = {player_won}, and computer won = {computer_won}."
            # quit()
            break
        elif user_input not in list_of_items:
            print("Please enter valid item next time. ")
            continue    # "continue takes to the top of the loop and loop recontinues. "
        elif user_input == computer_generated:
            print("It is a tie. ")
            tie += 1
            continue # "continue" takes to the top of the loop, and loop recontinues.
        elif user_input == "rock" and computer_generated == "paper":
            print("Computer won. ")
            computer_won += 1
            continue
        elif user_input == "paper" and computer_generated == "rock":
            print("you won. ")
            player_won += 1
            continue
        elif user_input == "rock" and computer_generated == "scissors":
            print("you won. ")
            player_won += 1
            continue
        elif user_input == "scissors" and computer_generated == "rock":
            print("Computer won. ")
            computer_won += 1
            continue
        elif user_input == "paper" and computer_generated == "scissors":
            print("Computer won. ")
            computer_won += 1
            continue
        elif user_input == "scissors" and computer_generated == "paper":
            print("you won. ")
            player_won += 1
            continue 
        else:
            break
    
    print(f"tie = {tie}, player won = {player_won}, and computer won = {computer_won}.")
    if player_won == computer_won:
        return "It's a tie; No body won it. "
    elif player_won > computer_won:
        return "Congratualtions you won it. "
    else:
        return "Computer won the game. "

print(rock_paper_scissors())


