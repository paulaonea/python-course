# Ask the user to enter the following three things using input() :
# - The amount they want to bet
# - A colour (red or black)
# - A number between 1 and 100
# After generating a random number and colour:
# - If the colour matches, the users keeps the amount that was bet
# - If the number matches, the users wins double the amount that was bet
# - If the colour and number matches, the users wins 100 times the amount that was bet When neither the colour or number
# matches the user wins 0
# Output the amount the user won


import random


def integer(message):
    choice = (input(message))
    while choice.isdigit() == False:
        choice = input(F'Not a valid choice. Try again. {message}')
    return choice


def color_choice(message):
    choice = input(message)
    while choice not in ['red', 'black']:
        choice = input(f'Not a valid choice. Try again. {message}: ')
    return choice


def number_choice(message):
    choice = integer(message)
    while choice not in range(1, 101, 1):
        print('Not a valid choice. Try again. ')
        choice = integer(message)
    return choice


def roulette():
    number = random.randint(1, 100)
    colour = random.choice(['red', 'black'])
    return number, colour


name = input('What is your name?: ').capitalize()
print(f'Hello {name}. This is a "roulette" type game, please make your choices.')
your_bet = integer(f'{name}, what amount do you want to bet? (integer number): ')
your_color = color_choice('Choose a colour (black or red): ')
your_number = number_choice('Choose a number between 1 and 100: ')

house = roulette()

if your_number == house[0] and your_color == house[1]:
        print(f'{name}, this is AWESOME! You have won {100 * your_bet}')
elif your_number == house[0]:
    print(f'{name}, this is your lucky day. You have won {2 * your_bet}')
elif your_color == house[1]:
    print(f'{name}, you have colour matching. You can keep your bet')
else:
    print(f'{name}, unfortunately you lost :(.  The house bet was {house[0]} {house[1]}.')

