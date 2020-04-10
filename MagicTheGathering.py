import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split


# Read from csv files
dataframe1 = pd.read_csv("./Datasets/secondEdition.csv")
dataframe2 = pd.read_csv("./Datasets/thirdEdition.csv")
dataframe3 = pd.read_csv("./Datasets/fourthEdition.csv")


# Convert raw data into a neat tables
dataframe1 = pd.DataFrame(dataframe1)
dataframe2 = pd.DataFrame(dataframe2)
dataframe3 = pd.DataFrame(dataframe3)


# PROVIDED LABELS FROM DATASET: 
    #  [name, manaCost, cmc, colorIdentity, artist, number, type, text, printings, flavor, layout, multiverseid, power, toughness, rarity, subtypes, types]
# WE WILL SELECT THE FOLLOWING: 
    # LABEL: EXAMPLE
    # name: 'Benalish Hero'
    # text: "Banding (Any creatures with banding, and up to one without, can attack in a band."
    # type: 'Creature — Human Soldier' 
    # power: '1' 
    # toughness:'1' 
    # manaCost: '{W}' 
    # colorIdentity: 'W'
X = dataframe1[['name', 'text', 'type', 'power', 'toughness', 'manaCost', 'colorIdentity']].dropna()#.to_numpy()
print(X)