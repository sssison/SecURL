import time
import pandas as pd                     # For data transformation
import numpy as numpy                   # For scientific calculations
import seaborn as sns                   # For data visualizations
import matplotlib.pyplot as plt         # For plotting
import plotly.graph_objects as go       # For plotting
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, classification_report
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, ConfusionMatrixDisplay
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline
import time
from datetime import datetime
import lexical_generator
import joblib

def rf_predict_maliciousness(url, i):

    rf_75 = joblib.load("rf_lexical_{}.sav".format(25*(i+1)))

    numerical_values = lexical_generator.lexical_generator(url)
    numerical_values = numerical_values.iloc[:, 0:(25*(i+1))]

    match rf_75.predict(numerical_values):
        case 0:
            return "Benign"
        case 1:
            return "Defacement"
        case 2:
            return "Phishing"
        case 3:
            return "Malware"
        
def xgb_predict_maliciousness(url, i):

    xgb_75 = XGBClassifier()
    xgb_75.load_model('xgb_lexical_{}.json'.format((25*(i+1))))

    numerical_values = lexical_generator.lexical_generator(url)
    numerical_values = numerical_values.iloc[:, 0:(25*(i+1))]

    match xgb_75.predict(numerical_values):
        case 0:
            return "Benign"
        case 1:
            return "Defacement"
        case 2:
            return "Phishing"
        case 3:
            return "Malware"

rf_results = []

for i in range(3):
    start = time.perf_counter()
    prediction = rf_predict_maliciousness("corporationwiki.com/Ohio/Columbus/frank-s-benson-P3333917.aspx",i)
    end = time.perf_counter()
    rf_results.append(((25*(i+1)), prediction,end-start))

rf_results = pd.DataFrame(rf_results, columns=['Number of Features','Prediction','Score Time'])
rf_results = rf_results.sort_values(by='Number of Features', ascending=True)
print(rf_results)

print("------------------------------------")

xgb_results = []

for i in range(3):
    start = time.perf_counter()
    prediction = xgb_predict_maliciousness("https://www.overleaf.com/project/657c1e9aa65bd48f6d65f413",i)
    end = time.perf_counter()
    xgb_results.append(((25*(i+1)), prediction,end-start))

xgb_results = pd.DataFrame(xgb_results, columns=['Number of Features','Prediction','Score Time'])
xgb_results = xgb_results.sort_values(by='Number of Features', ascending=True)
print(xgb_results)

