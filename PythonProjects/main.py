import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3d3914f6376607b43445109b687c9132'
HEADER = {'content-type' : 'application/json', 'trainer_token' :TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 12
}

body_change = {
    "pokemon_id": "347513",
    "name": "bylbik",
    "photo_id": 2
}

body_catch = {
    "pokemon_id": "347514"
}

body_battle = {
    "attacking_pokemon": "347514",
    "defending_pokemon": "347518"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

'''response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)
'''
'''response_battle = requests.post(url = f'{URL}/battle', headers = HEADER, json = body_battle)
print(response_battle.text)'''