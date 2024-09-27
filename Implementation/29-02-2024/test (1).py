import csv
import requests
import pandas as pd 
import matplotlib
import hashlib
import json
from PIL import Image
from io import BytesIO

pokemans = input("Enter A pokemon\n")
pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/'+pokemans) #Accesses The Url And Find Specific pokemon User Asks For (Stores It As Variable selfmon)
Info = json.loads(pokemon.text) #Turns pokemon Text Into Json, Can Be Used Like A Dictionary
print(Info)

sprite = requests.get('https://pokeapi.co/api/v2/pokemon/'+"sprites"+pokemans)
print(sprite)
            
sprites = requests.get('https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/icons/'+pokemans+'.png')
Image.open(BytesIO(sprites.content))