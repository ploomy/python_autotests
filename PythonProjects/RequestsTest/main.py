import requests


token = 'afb41f9b6ccc09d2cdde33c46d679fa6'
answer=requests.post('https://pokemonbattle.me:9104/pokemons', json = 
                      {
    "email":"ind-lidija-popova@qa.studio",
    "password": "-iG4npoFzxNWLZWcDlMf",
    "name": "Буль",
    "photo": "https://dolnikov.ru/pokemons/albums/006.png"
}, headers = {"trainer_token":token,
              "Content-Type" : "application/json"})

print(answer.text)

import requests

token = 'afb41f9b6ccc09d2cdde33c46d679fa6'
answer=requests.put('https://pokemonbattle.me:9104/pokemons', json = 
                      {
    "email":"ind-lidija-popova@qa.studio",
    "password": "-iG4npoFzxNWLZWcDlMf",
    "pokemon_id": "13064",
    "name": "Matehari",
    "photo": "https://dolnikov.ru/pokemons/albums/006.png"
}, headers = {"trainer_token":token,
              "Content-Type" : "application/json"})

print(answer.text)


import requests

token = 'afb41f9b6ccc09d2cdde33c46d679fa6'
answer=requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', json = 
                      {
    "email":"ind-lidija-popova@qa.studio",
    "password": "-iG4npoFzxNWLZWcDlMf",
    "pokemon_id": "13064",
    
}, headers = {"trainer_token":token,
              "Content-Type" : "application/json"})

print(answer.text)

