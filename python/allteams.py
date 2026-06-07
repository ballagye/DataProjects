
# Imports
import os
import polars as pl
import polars.selectors as cs
import matplotlib.pyplot as plt


# Création de la DataFrame et cleaning
_here = os.path.dirname(os.path.abspath(__file__))
df = pl.DataFrame(pl.read_csv(os.path.join(_here, "../data/NBA_DATASET/shootingdataperteam.csv")))
                  
df.filter(pl.all_horizontal(pl.all().is_null()))
df = df.drop("Unnamed: 0")

years = df.row(3)

print(type(years))
"""cleaned_df = df.iloc[3:35]
cleaned_df = cleaned_df.drop(columns=["Unnamed: 0"])



"""

















# Création de la variable years : x dans le plot et teams 
"""
years = cleaned_df.iloc[0]
years = years.dropna()
years = years = years.iloc[1:]
years = years.str.replace(r'-.*$', '', regex=True)
teams = cleaned_df.iloc[2:,0]
"""



# Nested loops, la première permet de récupérer les teams nba
# La deuxième va récupérer toutes les valeurs correspondant à 3PM pour chaque années dans le csv
"""
testdict = {}
for index, value, in teams.items():
    threePointersMadeList = []
    for index, threePointersMade in enumerate(cleaned_df.items(), start=3):
        if index % 4 == 0:
          threePointersMadeList.append(threePointersMade[1].iloc[1:])
    testdict[index, value] = threePointersMadeList
"""


   
   
