import pandas as pd

pokemon = pd.read_csv("Pokemon/pokemon.csv")

pokemon.rename(columns={"#" : "id"}, inplace=True)

pokemon = pokemon[["id", "Name", "Type 1"]]

