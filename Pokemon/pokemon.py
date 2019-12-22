# In this session you used the Pokemon API to retrieve a single Pokemon. I want a program that can retrieve multiple
# Pokemon and save their names and moves to a file. Use a list to store about 6 Pokemon IDs.
# Then in a for loop call the API to retrieve the data for each Pokemon.
# Save their names and moves into a file called 'pokemon.txt'

import requests
import json

def pokemon_details(pokemon_number):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_number}/'
    response = requests.get(url)
    pokemon = response.json()
    name = (pokemon['name'])
    moves = pokemon['moves']
    moves_names = []
    for value in moves:
        moves_names.append(value['move']['name'])
    return name, moves_names


pokemon_numbers = input("What are the pokemon's IDs?: (use space to delimit the numbers): ").split()  #returns a list of strings

with open('pokemons.txt', 'a+') as file:
    for pokemon_number in pokemon_numbers:
        pokemon_name, pokemon_moves = pokemon_details(pokemon_number)
        pokemon_dictionary = {pokemon_name: pokemon_moves}
        file.write(json.dumps(pokemon_dictionary) + "\n")





