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