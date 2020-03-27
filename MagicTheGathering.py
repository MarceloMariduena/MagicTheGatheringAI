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

# remove rows with missing values
dataframe1.dropna()
dataframe2.dropna()
dataframe3.dropna()

# testing
print(dataframe1)
