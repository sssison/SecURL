import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import feature_generation_lexical_function
from sklearn.feature_selection import f_classif, chi2, SelectKBest
import scipy.stats as stats

def anova_feature_selection(dataset):

       features = pd.read_csv(dataset)

       input_features = features.iloc[:, 1: ]
       numerical_features = input_features.drop(columns = ['get_tld', 'url_scheme'])

       url_class = features['url_type']

       anova_stats, anova_p = f_classif(numerical_features, url_class)
       #print('ANOVA Statistics: ')
       #print(anova_stats)
       #print('ANOVA P Values: ')
       #print(anova_p)

       feature_anova_stat = pd.Series(anova_stats)
       feature_anova_stat.index = numerical_features.columns
       feature_anova_stat = feature_anova_stat.sort_values(ascending = False)
       feature_anova_p = pd.Series(anova_p)
       feature_anova_p.index = numerical_features.columns
       pd.option_context('display.max_rows', None, 'display.max_columns', None)
       #print(feature_anova_stat.to_string())
       #print(feature_anova_p)

       return(feature_anova_stat.index.to_list(), feature_anova_stat.to_list())

def chi2_feature_selection(dataset):

       features = pd.read_csv(dataset)

       input_features = features.iloc[:, 1: ]
       categorical_features = input_features[['get_tld', 'url_scheme']]

       url_class = features['url_type']

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

def correlation_feature_selection(dataset):
       features = pd.read_csv(dataset)

       input_features = features.iloc[:, 1: ]

       input_features = input_features.drop(columns = ['get_tld', 'url_scheme'])

       corr = input_features.corr()

       highly_correlated = set()
       corr_threshold = 0.8
       for i in range(len(corr.columns)):
              for j in range(i):
                     if abs(corr.iloc[i, j]) > corr_threshold:
                            colname = corr.columns[i]
                            rowname = corr.index[j]
                            highly_correlated.add((colname, rowname))

       #print('Correlated features:' , highly_correlated)
       corr.to_csv('corr_matrix')
       #print(corr)
       return(highly_correlated)

if __name__ == '__main__':
       features, f_scores = anova_feature_selection('final_unbalanced_with_lexical.csv')
       features_f_scores = [(features[i], f_scores[i]) for i in range (len(features))]

       features_high_correlation = correlation_feature_selection('final_unbalanced_with_lexical.csv')

       f_scores = [i for i in f_scores if str(i) != 'nan']
       f_scores = np.array(f_scores)

       z_scores = stats.zscore(f_scores)

       percentile = []
       for z_score in z_scores:
              percentile.append(stats.norm.cdf(z_score))

       print('Feature Percentile: ')
       for i in range(len(percentile)):
              print(features[i], ': ', percentile[i])

       print('Correlated Features: ', features_high_correlation)