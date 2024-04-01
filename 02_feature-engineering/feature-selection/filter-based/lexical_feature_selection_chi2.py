import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import feature_generation_lexical_function
from sklearn.feature_selection import chi2, SelectKBest, f_classif

lexical_features = pd.read_csv('final_unbalanced_with_lexical.csv')
print(lexical_features)
print(lexical_features.info())

input_features = lexical_features[['get_tld', 'url_scheme']]
print(input_features)

classification = lexical_features['url_type']
print(classification)

chi2_stat, p_val = chi2(input_features, classification)

print('Chi2 Statistics:')
print(chi2_stat)
print('P Values:')
print(p_val)