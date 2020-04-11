# Read from csv files convert contents into tables.
import pandas as pd
dataframe1 = pd.read_csv("./Datasets/secondEdition.csv")
dataframe2 = pd.read_csv("./Datasets/thirdEdition.csv")
dataframe3 = pd.read_csv("./Datasets/fourthEdition.csv")
dataframe1 = pd.DataFrame(dataframe1)
dataframe2 = pd.DataFrame(dataframe2)
dataframe3 = pd.DataFrame(dataframe3)


# Select the categories we will deal with. Ensure rows with missing data are not used.
X = dataframe1[['text', 'type', 'power', 'toughness', 'manaCost', 'colorIdentity']].dropna().to_numpy()
card_text = list(X[:,0])
card_type = list(X[:,1])
card_power = list(X[:,2])
card_toughness = list(X[:,3])
card_mana_cost = list(X[:,4])
card_color_identity = list(X[:,5])


# Train the model, CountVectorizer:
    # Given that descriptions are series of ordered words, we can convert those series into numerical feature vectors
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(card_text)
X_train_counts.shape


# Reduce the weightage of certain words like (the, is, a, an, etc) 
    # For this we will use Term Frequency times inverse document frequency (TfidTransformer) to invert the stats and return keywords. 
from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape


# # Encode the targets
# from sklearn import preprocessing
# card_type_encoder = preprocessing.LabelEncoder()
# card_power_encoder = preprocessing.LabelEncoder()
# card_toughness_encoder = preprocessing.LabelEncoder()
# card_mana_cost_encoder = preprocessing.LabelEncoder()
# card_color_identity_encoder = preprocessing.LabelEncoder()


# Now we can begin the classification with various targets
from sklearn.naive_bayes import MultinomialNB
clf1 = MultinomialNB().fit(X_train_tfidf, card_type)
clf2 = MultinomialNB().fit(X_train_tfidf, card_power)
clf3 = MultinomialNB().fit(X_train_tfidf, card_toughness)
clf4 = MultinomialNB().fit(X_train_tfidf, card_mana_cost)
clf5 = MultinomialNB().fit(X_train_tfidf, card_color_identity)


# Test data 
X2 = dataframe2[['text', 'type', 'power', 'toughness', 'manaCost', 'colorIdentity']].dropna().to_numpy()
card_text2 = list(X2[:,0])
card_type2 = list(X2[:,1])
card_power2 = list(X[:,2])
card_toughness2 = list(X[:,3])
card_mana_cost2 = list(X[:,4])
card_color_identity2 = list(X[:,5])


# Training other classifiers
from sklearn.pipeline import Pipeline

text_clf = Pipeline([
    ('vect', CountVectorizer()), 
    ('tfidf', TfidfTransformer()), 
    ('clf', MultinomialNB()),
])
text_clf = text_clf.fit(card_text, card_type)

from sklearn.linear_model import SGDClassifier
text_clf_svm = Pipeline([
    ('vect', CountVectorizer()), 
    ('tfidf', TfidfTransformer()), 
    ('clf-svm', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42))
    ,])
text_clf_svm = text_clf_svm.fit(card_text, card_type)


# Accuracy testing
import numpy as np
predicted = text_clf.predict(card_text2)
print(np.mean(predicted == card_type2))

predicted_svm = text_clf_svm.predict(card_text2)
print(np.mean(predicted_svm == card_type2))

