import numpy as np
import pandas as pd
import json
# Given that descriptions are series of ordered words, we can convert those series into numerical feature vectors
from sklearn.feature_extraction.text import CountVectorizer
# Reduce the weightage of certain words like (the, is, a, an, etc) 
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
import pickle

# Read from csv files convert contents into tables.
dataframe1 = pd.read_csv("./Datasets/secondEdition.csv")
dataframe2 = pd.read_csv("./Datasets/thirdEdition.csv")
dataframe3 = pd.read_csv("./Datasets/fourthEdition.csv")
dataframe1 = pd.DataFrame(dataframe1)
dataframe2 = pd.DataFrame(dataframe2)
dataframe3 = pd.DataFrame(dataframe3)


# Select the categories we will deal with. Ensure rows with missing data are not used.
X = dataframe1[['text', 'type', 'power', 'toughness', 'manaCost', 'colorIdentity']].dropna().to_numpy()

# Futher filtering: drop rows with less than 10 words. 
raw_X1 = dataframe1[['text', 'type', 'power', 'toughness', 'manaCost', 'colorIdentity']].dropna().to_numpy()
raw_X2 = dataframe3[['text', 'type', 'power', 'toughness', 'manaCost', 'colorIdentity']].dropna().to_numpy()
X = np.concatenate((raw_X1, raw_X2), axis=0)


card_text = list(X[:,0])
card_type = list(X[:,1]) # target1
card_power = list(X[:,2]) # target2
card_toughness = list(X[:,3]) # target3
card_mana_cost = list(X[:,4]) # target4
card_color_identity = list(X[:,5]) # target5


# Train the models
text_clf_svm1 = Pipeline([
    ('vect', CountVectorizer()), 
    ('tfidf', TfidfTransformer()), 
    ('clf-svm', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42))
    ,])
text_clf_svm1 = text_clf_svm1.fit(card_text, card_type)

text_clf_svm2 = Pipeline([
    ('vect', CountVectorizer()), 
    ('tfidf', TfidfTransformer()), 
    ('clf-svm', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42))
    ,])
text_clf_svm2 = text_clf_svm2.fit(card_text, card_power)

text_clf_svm3 = Pipeline([
    ('vect', CountVectorizer()), 
    ('tfidf', TfidfTransformer()), 
    ('clf-svm', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42))
    ,])
text_clf_svm3 = text_clf_svm3.fit(card_text, card_toughness)

text_clf_svm4 = Pipeline([
    ('vect', CountVectorizer()), 
    ('tfidf', TfidfTransformer()), 
    ('clf-svm', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42))
    ,])
text_clf_svm4 = text_clf_svm4.fit(card_text, card_mana_cost)

text_clf_svm5 = Pipeline([
    ('vect', CountVectorizer()), 
    ('tfidf', TfidfTransformer()), 
    ('clf-svm', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42))
    ,])
text_clf_svm5 = text_clf_svm5.fit(card_text, card_color_identity)


# Test data 
X2 = dataframe2[['text', 'type', 'power', 'toughness', 'manaCost', 'colorIdentity']].dropna().to_numpy()
card_text2 = list(X2[:,0])
card_type2 = list(X2[:,1])
card_power2 = list(X2[:,2])
card_toughness2 = list(X2[:,3])
card_mana_cost2 = list(X2[:,4])
card_color_identity2 = list(X2[:,5])


## Accuracy testing: Mean scores
# predicted_svm1 = text_clf_svm1.predict(card_text2)
# print('Type: ', (np.mean(predicted_svm1 == card_type2) * 100), '%')

# predicted_svm2 = text_clf_svm2.predict(card_text2)
# print('Power: ', (np.mean(predicted_svm2 == card_power2) * 100), '%')

# predicted_svm3 = text_clf_svm3.predict(card_text2)
# print('Toughness: ', (np.mean(predicted_svm3 == card_toughness2) * 100), '%')

# predicted_svm4 = text_clf_svm4.predict(card_text2)
# print('Mana cost: ', (np.mean(predicted_svm4 == card_mana_cost2) * 100), '%')

# predicted_svm5 = text_clf_svm5.predict(card_text2)
# print('Color identity: ', (np.mean(predicted_svm5 == card_color_identity2) * 100), '%')


# User 
userName = input("Enter your name:\n>>")
userDescription = list(input("Tell me about yourself, big boy/girl:\n>>"))

userType = list(text_clf_svm1.predict(userDescription))
userPower = list(text_clf_svm2.predict(userDescription))
userToughness = list(text_clf_svm3.predict(userDescription))
userMana = list(text_clf_svm4.predict(userDescription))
userColor = list(text_clf_svm5.predict(userDescription))


'''
#model generation
with open('type_model.obj','wb') as f:
    pickle.dump(text_clf_svm1,f)

with open('power_model.obj','wb') as f:
    pickle.dump(text_clf_svm2,f)

with open('tough_model.obj','wb') as f:
    pickle.dump(text_clf_svm3,f)

with open('mana_model.obj','wb') as f:
    pickle.dump(text_clf_svm4,f)

with open('color_model.obj','wb') as f:
    pickle.dump(text_clf_svm5,f)
'''


print('\nWell then young warrior! You are a %s %s of with a power level of %s, a tougness of %s, and a mana cost of %s.' % (userColor[0], userType[0], userPower[0], userToughness[0], userMana[0]))

user_results = {
    "color": userColor[0], 
    "type": userType[0], 
    "power": userPower[0], 
    "toughness": userToughness[0], 
    "mana": userMana[0]
}

# Format output to JSON file
with open('userStats.json', 'w') as f:
    json.dump(user_results, f, ensure_ascii=False, indent=4)

# TODO: 
# * increase accuracy of model (DONE)
# * format output into JSON file (DONE)
# * look into running runway over the web