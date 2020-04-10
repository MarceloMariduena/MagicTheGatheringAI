#! resources: https://pd.pydata.org/pd-docs/stable/reference/api/pd.DataFrame.dropna.html

# TODO: App
# 1. Allow user to input photo, [ name, text ].
# 2. Return a MagicTheGathering card with:
#       2.1. *Animated (MagicTheGathering) photo of the user
#       2.1. name
#       2.1. text
#       2.1. type
#       2.1. power
#       2.1. toughness
#       2.1. manaCost
#       2.1. colorIdentity


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


# LABELS TO WORK WITH: !userWillInput *modelOutput
#   !name, !text, *type, *power, *toughness, *manaCost, *colorIdentity


# SELECTING FEATURES 
features = dataframe1[['name', 'text', 'type', 'power', 'toughness', 'manaCost', 'colorIdentity']].dropna()


# SPLIT DATA INTO SETS:
#   X: inputs
#   y: outputs
X = dataframe1[['name', 'text']].dropna() 
y = dataframe1[['type', 'power', 'toughness', 'manaCost', 'colorIdentity']].dropna() 

# print(y)
X = np.array(X)
y = np.array(y)

# Pre Processing Text


textEncoder = preprocessing.LabelEncoder()
iteration = 1
for row in X[1:,1]:
    holder = ""
    lister = []
    for x in row:
        if(x ==" "):
           # print(x+ "IS THE LAST CHAR OF : "+holder)
            textEncoder.fit_transform([holder])
            lister.append(holder)
            holder = ""
        else:
            holder=holder+x 
    X[iteration,1] = lister
   # print(X[iteration,1]) 
    iteration=iteration+1
       
print(X[:,1])
























