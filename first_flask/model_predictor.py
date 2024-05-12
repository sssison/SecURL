import pandas as pd                     # For data transformation
import numpy as numpy                   # For scientific calculations
import seaborn as sns                   # For data visualizations
import matplotlib.pyplot as plt         # For plotting
import plotly.graph_objects as go       # For plotting
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, classification_report
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, ConfusionMatrixDisplay
from xgboost import XGBClassifier, DMatrix, train
from sklearn.pipeline import Pipeline
import time
from datetime import datetime
import joblib
import os


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