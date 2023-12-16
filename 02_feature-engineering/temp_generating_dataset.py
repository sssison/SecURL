import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import temp_featuregen
import temp_featuregen_2

dataset = pd.read_csv("final_dataset_noFeatures.csv")

dataset["url_type"] = dataset["type"].replace({
    'benign':0,
    'defacement':1,
    'phishing':2,
    'malware':3
});
print("Type Replaced...")

# Insert Feature Generation
dataset['url_length'] = dataset['url'].apply(lambda x: temp_featuregen.get_url_length(x))
print("Feature 1 Done...")

# dataset['pri_domain'] = dataset['url'].apply(lambda x: temp_featuregen.extract_pri_domain(x))
print("Feature 2 Left Out...")

dataset['letter_count'] = dataset['url'].apply(lambda x: temp_featuregen.count_letters(x))
print("Feature 3 Done...")

dataset['digits_count'] = dataset['url'].apply(lambda x: temp_featuregen.count_digits(x))
print("Feature 4 Done...")

dataset['special_char_count'] = dataset['url'].apply(lambda x: temp_featuregen.count_special_chars(x))
print("Feature 5 Done...")

# Features 6 to 20
# Can probably make features 6 to 17 an iterative process

dataset['._count'] = dataset['url'].apply(lambda x: temp_featuregen_2.get_char_count(x, '.'))
print("Feature 6 Done...")

dataset['-_count'] = dataset['url'].apply(lambda x: temp_featuregen_2.get_char_count(x, '-'))
print("Feature 7 Done...")

dataset['__count'] = dataset['url'].apply(lambda x: temp_featuregen_2.get_char_count(x, '_'))
print("Feature 8 Done...")

dataset['=_count'] = dataset['url'].apply(lambda x: temp_featuregen_2.get_char_count(x, '='))
print("Feature 9 Done...")

dataset['/_count'] = dataset['url'].apply(lambda x: temp_featuregen_2.get_char_count(x, '/'))
print("Feature 10 Done...")

dataset['?_count'] = dataset['url'].apply(lambda x: temp_featuregen_2.get_char_count(x, '?'))
print("Feature 11 Done...")

dataset[';_count'] = dataset['url'].apply(lambda x: temp_featuregen_2.get_char_count(x, ';'))
print("Feature 12 Done...")

dataset['(_count'] = dataset['url'].apply(lambda x: temp_featuregen_2.get_char_count(x, '('))
print("Feature 13 Done...")

dataset[')_count'] = dataset['url'].apply(lambda x: temp_featuregen_2.get_char_count(x, ')'))
print("Feature 14 Done...")

dataset['%_count'] = dataset['url'].apply(lambda x: temp_featuregen_2.get_char_count(x, '%'))
print("Feature 15 Done...")

dataset['&_count'] = dataset['url'].apply(lambda x: temp_featuregen_2.get_char_count(x, '&'))
print("Feature 16 Done...")

dataset['@_count'] = dataset['url'].apply(lambda x: temp_featuregen_2.get_char_count(x, '@'))
print("Feature 17 Done...")

# Dropping type and url
dataset = dataset.drop(columns = ['url', 'type'])

print("Removing Duplicates")
dataset.drop_duplicates(inplace = True)

dataset.to_csv("temp_dataset_withFeatures.csv", encoding='utf-8', index=False)
dataset.to_csv("../03_machine-learning-model/temp_dataset_withFeatures.csv", encoding='utf-8', index=False)