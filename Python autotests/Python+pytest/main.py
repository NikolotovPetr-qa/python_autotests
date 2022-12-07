import requests
import json

token = '951367b81de4ab5c616e5af8929c1920'

response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer-token': token}, json = {
    "name": "ИванДраго",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"

})
print(response.text)

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer-token': token}, json = {
    "pokemon_id": 1431, 
    "name": "ИванНеДраго",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})
print(response_put.text)

response_addPokeball = requests.post('https://pokemonbattle.me:5000/trainers/addPokebol', headers ={'trainer-token': token}, json = {
    'pokemon_id': 1431
})
print(response_addPokeball.text)