import requests

token = 'afb41f9b6ccc09d2cdde33c46d679fa6'
host = 'https://pokemonbattle.me:9104'

answer = requests.get(f'{host}/trainers', json = 
                      {
    "email":"ind-lidija-popova@qa.studio",
    "password": "-iG4npoFzxNWLZWcDlMf",
    }, headers = {"trainer_token":token,
              "Content-Type": "application/json",
              "trainer_id":4351})
print(answer.text)
