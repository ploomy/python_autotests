import requests
import pytest

token = 'afb41f9b6ccc09d2cdde33c46d679fa6'
host = 'https://pokemonbattle.me:9104'
def test_status_code():
    answer = requests.get(f'{host}/trainers', json = 
                      {
    "email":"ind-lidija-popova@qa.studio",
    "password": "-iG4npoFzxNWLZWcDlMf",
    }, headers = {"trainer_token":token,
              "Content-Type" : "application/json"})
    assert answer.status_code == 200


import requests
import pytest

token = 'afb41f9b6ccc09d2cdde33c46d679fa6'
host = 'https://pokemonbattle.me:9104'
def test_trainer_name():
    answer_body = requests.get(f'{host}/trainers', params={"trainer_id": "4351"}, json=
                               {
    "email": "ind-lidija-popova@qa.studio",
    "password": "-iG4npoFzxNWLZWcDlMf",
    }, headers={"trainer_token": token,
            "Content-Type": "application/json"
        })
    assert answer_body.json()['trainer_name'] == 'Zombi'