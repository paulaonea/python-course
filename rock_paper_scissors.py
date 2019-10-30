# Rock, paper, scissors game.
# you can choose to play against a friend or against the computer.
# if you choose to play against the computer, the computer's choice will be generated randomly.

import random


def choice(name):
    text = input(f'{name}, please choose rock, paper or scissors: ')
    while text not in ['rock', 'paper', 'scissors']:
        text = input(f'{name}, your choice is not valid, please choose again (rock, paper, scissors): ')
    return text


def result(choice1, choice2):
    winning_combinations = [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')] # first object in the tuple is the winner
    if choice1 == choice2:
        return 'draw'
    elif (choice1, choice2) in winning_combinations:
        return 'won'
    else:
        return 'lost'


your_name = input('What is your name?: ')
print(f'Hello {your_name}. This is Rock, Paper, Scissors game. You can play against a friend or against the computer.')
opponent = input(f'Do you want to play against the computer? (y/n) ')
if opponent == 'n':
    friend_name = input(f'{your_name}, you chose to play against a friend. What is your friend\'s name?: ')

your_choice = choice(your_name)

if opponent == 'n':
    opponent_choice = choice(friend_name)
else:
    opponent_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f'Your opponent chose {opponent_choice}.')

game_result = result(your_choice, opponent_choice)
if game_result == 'draw':
    print(f'The game resulted in DRAW.')
else:
    print(f'{your_name}, you {game_result}!')



