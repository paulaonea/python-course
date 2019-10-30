# Rock, paper, scissors game.
# you can choose to play against a friend or against the computer.
# if you choose to play against the computer, the computer's choice will be generated randomly.


import random

def random_choice():
    choices = ['rock', 'paper', 'scissors']
    return choices[random.randint(0, 2)]


def result(choice1, choice2):
    winners = [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]
    if (choice1, choice2) in winners:
        return 'won'
    else:
        return 'lost'


your_name = input('What is your name?: ')
print(f'Hello {your_name}. This is Rock, Paper, Scissors game. You can play against a friend or against the computer.')
opponent = input(f'Please choose your opponent: (computer / friend) ')
if opponent.lower() == 'friend':
    friend_name = input(f'What is your friend\'s name?: ')

your_choice = input(f'{your_name}, please choose rock, scissors or paper: ')
if opponent.lower() == 'friend':
    opponent_choice = input(f'{friend_name}, please choose rock, scissors or paper: ')
else:
    opponent_choice = random_choice()
    print(f'Your opponent chose {opponent_choice}.')

game_result = result(your_choice, opponent_choice)
print(f'{your_name} you {game_result}.')



