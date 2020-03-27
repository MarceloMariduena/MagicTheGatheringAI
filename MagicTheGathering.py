import numpy 
import pandas 

# read the csv file 
dataframe = pandas.read_csv("./secondEdition.csv")
dataset = dataframe.values
print(dataset)
