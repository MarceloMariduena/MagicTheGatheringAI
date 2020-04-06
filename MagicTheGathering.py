#! resources: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html

import numpy 
import pandas 

# read the csv file 
dataframe1 = pandas.read_csv("./secondEdition.csv")
dataframe2 = pandas.read_csv("./thirdEdition.csv")
dataframe3 = pandas.read_csv("./fourthEdition.csv")

# convert it into a neat table 
dataframe1 = pandas.DataFrame(dataframe1)
dataframe2 = pandas.DataFrame(dataframe2)
dataframe3 = pandas.DataFrame(dataframe3)


features = dataframe1[['type', 'subtypes', 'rarity']].dropna()
print(features)


# TODO: Code
# 1. Get a dataset
# 2. Encode features
# 3. Take user input (Name, Description, Mana cost)
# 4. Generate the following:
#       4.1. Effects
#       4.2. Type
#       4.3. Health
#       4.4. Power


# TODO: App
# 1. Allow user to input photo, name, description, mana cost.
# 2. Return a MagicTheGathering card with:
#       2.1. *Animated (MagicTheGathering) photo of the user
#       2.1. Name
#       2.1. Description
#       2.1. Mana cost
#       2.1. *Effects
#       2.1. *Type
#       2.1. *Health
#       2.1. *Power