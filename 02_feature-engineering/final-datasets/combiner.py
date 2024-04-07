import pandas as pd                     # For data transformation
import numpy as numpy                   # For scientific calculations
import seaborn as sns                   # For data visualizations
import matplotlib.pyplot as plt         # For plotting
import plotly.graph_objects as go       # For plotting

dataset_1 = pd.read_csv("final_unbalanced_withLexical.csv")
dataset_2 = pd.read_csv("temp_unbalanced_with_lexical.csv")
dataset_3 = pd.read_csv("newdata_unbalanced_with_lexical.csv")

dataset_2["url_type"] = dataset_2["type"]
dataset_2 = dataset_2.drop(columns = ['type'])

dataset_1["url_type"] = dataset_1["url_type"].replace({
    0:0,
    1:1,
    2:1,
    3:1,
});

final_unbalanced = pd.concat([dataset_1, dataset_2, dataset_3])        # Merges all of the datasets
final_unbalanced.drop_duplicates(inplace=True)

final_unbalanced.to_csv("binary_combined_new_Bacud_unbalanced_lexical.csv", encoding='utf-8', index=False)