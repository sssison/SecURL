import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import feature_generation_lexical_function
from sklearn.feature_selection import f_classif, SelectKBest

lexical_features = pd.read_csv('final_unbalanced_with_lexical.csv')
print(lexical_features)
print(lexical_features.info())

input_features = lexical_features.iloc[:, 1: ]
print(input_features)

classification = lexical_features['url_type']
print(classification)

f_score, p_val = f_classif(input_features, classification)

print('F Score:')
print(f_score)
print('P Value:')
print(p_val)

features_f_score = pd.Series(f_score)
features_f_score.index = input_features.columns
print(features_f_score)