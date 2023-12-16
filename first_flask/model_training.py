import re
import nltk
import tldextract
import hashlib
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from colorama import Fore
from urllib.parse import urlparse
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, classification_report
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, ExtraTreesClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB
from tld import get_tld, is_tld
from tld.exceptions import TldDomainNotFound, TldBadUrl, TldIOError
import logging
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier
import whois
from sklearn.pipeline import Pipeline
from datetime import datetime
from plotly.subplots import make_subplots
from wordcloud import WordCloud
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier, ExtraTreesClassifier, BaggingClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.neural_network import MLPClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans
from sklearn.linear_model import RidgeClassifier, Perceptron, SGDClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import temp_featuregen
import feature_generation
import time

# Load the Dataset
dataset = pd.read_csv('malicious_phish.csv')
print("Dataset loaded...")

dataset["url_type"] = dataset["type"].replace({
    'benign':0,
    'defacement':1,
    'phishing':2,
    'malware':3
});
print("Type Replaced...")

# Insert Feature Generation
dataset['url_length'] = dataset['url'].apply(lambda x: temp_featuregen.get_url_length(x))
print("Feature 1 Done...")

# dataset['pri_domain'] = dataset['url'].apply(lambda x: temp_featuregen.extract_pri_domain(x))
print("Feature 2 Left Out...")

dataset['letter_count'] = dataset['url'].apply(lambda x: temp_featuregen.count_letters(x))
print("Feature 3 Done...")

dataset['digits_count'] = dataset['url'].apply(lambda x: temp_featuregen.count_digits(x))
print("Feature 4 Done...")

dataset['special_char_count'] = dataset['url'].apply(lambda x: temp_featuregen.count_special_chars(x))
print("Feature 5 Done...")

# Features 6 to 20
# Can probably make features 6 to 17 an iterative process

dataset['._count'] = dataset['url'].apply(lambda x: feature_generation.get_char_count(x, '.'))
print("Feature 6 Done...")

dataset['-_count'] = dataset['url'].apply(lambda x: feature_generation.get_char_count(x, '-'))
print("Feature 7 Done...")

dataset['__count'] = dataset['url'].apply(lambda x: feature_generation.get_char_count(x, '_'))
print("Feature 8 Done...")

dataset['=_count'] = dataset['url'].apply(lambda x: feature_generation.get_char_count(x, '='))
print("Feature 9 Done...")

dataset['/_count'] = dataset['url'].apply(lambda x: feature_generation.get_char_count(x, '/'))
print("Feature 10 Done...")

dataset['?_count'] = dataset['url'].apply(lambda x: feature_generation.get_char_count(x, '?'))
print("Feature 11 Done...")

dataset[';_count'] = dataset['url'].apply(lambda x: feature_generation.get_char_count(x, ';'))
print("Feature 12 Done...")

dataset['(_count'] = dataset['url'].apply(lambda x: feature_generation.get_char_count(x, '('))
print("Feature 13 Done...")

dataset[')_count'] = dataset['url'].apply(lambda x: feature_generation.get_char_count(x, ')'))
print("Feature 14 Done...")

dataset['%_count'] = dataset['url'].apply(lambda x: feature_generation.get_char_count(x, '%'))
print("Feature 15 Done...")

dataset['&_count'] = dataset['url'].apply(lambda x: feature_generation.get_char_count(x, '&'))
print("Feature 16 Done...")

dataset['@_count'] = dataset['url'].apply(lambda x: feature_generation.get_char_count(x, '@'))
print("Feature 17 Done...")

# dataset['tld'] = dataset['url'].apply(lambda x: feature_generation.get_tld(urlparse(x)))
# print("Feature 18 Done...")

# dataset['ip_address'] = dataset['url'].apply(lambda x: feature_generation.get_ip(urlparse(x)))
# print("Feature 19 Done...")

# dataset['query_len'] = dataset['url'].apply(lambda x: feature_generation.get_query_len(urlparse(x)))
# print("Feature 20 Done...")

# Dropping type and url
dataset = dataset.drop(columns = ['url', 'type'])

print("Removing Duplicates")
dataset.drop_duplicates(inplace = True)

# Insert Feature Reduction

# Dividing the dataset for validation.
url_features = dataset.drop(columns = ['url_type'])
url_type = dataset['url_type']

url_features_train,url_features_test,url_type_train,url_type_test = train_test_split(url_features,url_type,test_size=0.3, random_state=42)
print("Dataset Divided...")

results = []

print("Starting Training...")
for i in range(4):
    pipeline = Pipeline([('classifier', RandomForestClassifier())])

    temp_url_features = url_features.iloc[:, 0:(4*(i+1))]

    start = time.perf_counter()

    scores = cross_val_score(pipeline, temp_url_features, url_type, cv = 2, scoring = 'accuracy')
    url_type_predict = cross_val_predict(pipeline, temp_url_features, url_type, cv=2)

    end = time.perf_counter()

    prediction_time = end-start

    accuracy = accuracy_score(url_type, url_type_predict)
    recall = recall_score(url_type, url_type_predict, average = 'weighted')
    precision = precision_score(url_type, url_type_predict, average = 'weighted', zero_division=1)
    f1 = f1_score(url_type, url_type_predict, average = 'weighted')
    results.append(((4*(i+1)), accuracy, recall, precision, f1, prediction_time))
    print("Model {0} Done...".format(i+1))

results = pd.DataFrame(results, columns=['Number of Features', 'Accuracy', 'Recall', 'Precision', 'F1-Score', 'Training Time'])
results = results.sort_values(by='Accuracy', ascending=False)
print(results.head())

'''
# Model Training

print("Starting Training...")
pipeline = Pipeline([('classifier', RandomForestClassifier())])

pipeline.fit(url_features_train, url_type_train)
print("Finished Training...")

print("Predicting...")
url_type_predict = pipeline.predict(url_features_test)

print("Printing Report...")
print(classification_report(url_type_test, url_type_predict))
'''

# Save model


