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
        
def xgb_predict_maliciousness(url):

    xgb_ffs_12 = XGBClassifier()
    xgb_ffs_12.load_model('xgb_ffs_12.sav')

    numerical_values = lexical_generator.lexical_generator(url)

    match xgb_ffs_12.predict(numerical_values):
        case 0:
            return "Benign"
        case 1:
            return "Defacement"
        case 2:
            return "Phishing"
        case 3:
            return "Malware"

url = "https://www.facebook.com/"
print("Current URL: "+url)

start = time.perf_counter()
prediction = xgb_predict_maliciousness(url)
end = time.perf_counter()

print(prediction)
print(end-start)