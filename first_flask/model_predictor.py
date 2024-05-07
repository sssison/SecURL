import pickle
import joblib
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
import time


def predict_maliciousness_lexical(url_features):
    """
    The function `predict_maliciousness_lexical` loads a saved XGBoost model and predicts whether a URL
    is benign or malicious based on lexical features.
    
    :param url_features: It looks like the code snippet you provided is a function called
    `predict_maliciousness_lexical` that loads a saved XGBoost model and uses it to predict whether a
    given URL is benign or malicious based on the provided `url_features`
    """

    pipeline = joblib.load("model/xgb_wrapper_33_lexical.sav")

    match pipeline.predict(url_features):
            case 0:
                return "Benign*"
            case 1:
                return "Malware*"
        
def predict_maliciousness_content(url_features):
    """
    The function `predict_maliciousness_content` loads a machine learning model and predicts whether a
    given URL content is benign or malicious.
    
    :param url_features: It looks like you are trying to define a function
    `predict_maliciousness_content` that takes `url_features` as input and uses a pre-trained XGBoost
    model to predict whether the content is benign or malicious
    """

    pipeline = joblib.load("model/xgb_wrapper_65_lexical-content.sav")

    match pipeline.predict(url_features):
            case 0:
                return "Benign*"
            case 1:
                return "Malware*"