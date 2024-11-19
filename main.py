import csv
import os

import requests

from pokemon import PokemonEntry

os.system("mkdir -p output")
res = requests.get("https://pokemon-go-api.github.io/pokemon-go-api/api/pokedex.json")
data = res.json()
if data:
    with open("output/pokemon-go.csv", "a") as fileptr:
        header = [
            "Pokedex #",
            "Name",
            "Generation",
            "Class",
            "Image",
            "Caught?",
            "Shiny Image",
            "Shiny Caught?",
            "Regional Forms",
        ]
        writer = csv.writer(fileptr)
        writer.writerow(header)

        for asset in data:
            pokemon = PokemonEntry(asset)
            pokemon.write_to_sheet(writer)
