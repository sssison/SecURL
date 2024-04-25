import pandas as pd
from mlxtend.feature_selection import SequentialFeatureSelector
from xgboost import XGBClassifier
import matplotlib.pyplot as plt
import numpy as np

def xgb_ffs(dataset_csv):
    dataset = pd.read_csv(dataset_csv)
    features = dataset.iloc[:, 1:]
    url_type = dataset.iloc[:, 0]

    forward_feature_selection = SequentialFeatureSelector(XGBClassifier(), k_features = 113, forward = True,
                                                      floating = False, verbose = 10, scoring = 'accuracy', n_jobs = 1).fit(features, url_type)
    
    all_iterations = pd.DataFrame.from_dict(forward_feature_selection.get_metric_dict()).T
    score_series = pd.Series(all_iterations['avg_score'])
    score_list = score_series.to_list()

    plateau_dict = {}
    prev = score_list[0]
    plateau_dict[score_list.index(prev)] = 1
    for accuracy in score_list[1:]:
        if accuracy > prev*1.001:
            prev = accuracy
            plateau_dict[score_list.index(prev)] = 1
            pass
        else:
            plateau_dict[score_list.index(prev)] += 1

    longest_plateau = max(plateau_dict, key = plateau_dict.get)

    feature_series = pd.Series(all_iterations['feature_names'])
    feature_list = feature_series.to_list()

    reduced_feature_list = list(feature_list[longest_plateau])

    return reduced_feature_list

if __name__ == '__main__':
    print(xgb_ffs('binary_unbalanced_with_content.csv'))