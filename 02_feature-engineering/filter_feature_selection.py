import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import feature_generation_lexical_function
from sklearn.feature_selection import f_classif, chi2, SelectKBest

features = pd.read_csv('final_unbalanced_with_lexical.csv')

input_features = features.iloc[:, 1: ]
numerical_features = input_features.drop(columns = ['get_tld', 'url_scheme'])
categorical_features = input_features[['get_tld', 'url_scheme']]

url_class = features['url_type']

anova_stats, anova_p = f_classif(numerical_features, url_class)
print('ANOVA Statistics: ')
print(anova_stats)
print('ANOVA P Values: ')
print(anova_p)

feature_anova_stat = pd.Series(anova_stats)
feature_anova_stat.index = numerical_features.columns
feature_anova_stat = feature_anova_stat.sort_values(ascending = False)
feature_anova_p = pd.Series(anova_p)
feature_anova_p.index = numerical_features.columns
pd.option_context('display.max_rows', None, 'display.max_columns', None)
print(feature_anova_stat.to_string())
print(feature_anova_p)

chi2_stats, chi2_p = chi2(categorical_features, url_class)
print('Chi2 Statistics: ')
print(chi2_stats)
print('Chi2 P Values: ')
print(chi2_p)

feature_chi2_stat = pd.Series(chi2_stats)
feature_chi2_stat.index = categorical_features.columns
feature_chi2_stat = feature_chi2_stat.sort_values(ascending = False)
feature_chi2_p = pd.Series(chi2_p)
feature_chi2_p.index = categorical_features.columns
pd.option_context('display.max_rows', None, 'display.max_columns', None)
print(feature_chi2_stat.to_string())
print(feature_chi2_p)

corr = input_features.corr()

print(corr)
