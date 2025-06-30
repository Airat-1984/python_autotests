import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3d3914f6376607b43445109b687c9132'
HEADER = {'content-type' : 'application/json', 'trainer_token' :TOKEN}
TRAINER_ID = '36089'

def test_status_cod():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'мастер ЛИ'


    