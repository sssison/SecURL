import pandas as pd
from feature_generation_content_function_htmlin import get_html

dataset = pd.read_csv('dataset_split4.csv') #REPLACE N WITH YOUR SPLIT

dataset['type'] = dataset['type'].replace({
    'benign' : 0,
    'defacement': 1,
    'phishing': 2,
    'malware': 3,
})

dataset['html'] = dataset['url'].apply(lambda x: get_html(x))
dataset = dataset.dropna()

dataset.to_csv("dataset_split4_cleansed.csv", encoding='utf-8', index=False) #REPLACE N WITH YOUR SPLIT