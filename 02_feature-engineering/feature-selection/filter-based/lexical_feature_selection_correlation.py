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

corr = lexical_features.corr()
a = sns.heatmap(corr)