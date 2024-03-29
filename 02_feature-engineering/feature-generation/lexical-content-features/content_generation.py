import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import feature_generation_content_function_htmlin
from datetime import datetime
from feature_generation_content_function_htmlin import get_html

dataset = pd.read_csv('final_unbalanced_noFeatures.csv')

dataset['type'] = dataset['type'].replace({
    'benign' : 0,
    'defacement': 1,
    'phishing': 2,
    'malware': 3,
})

dataset['html'] = dataset['url'].apply(lambda x: get_html(x))
dataset = dataset.dropna()

print(dataset)
print(dataset.info())

s = datetime.now()

print('Feature 1 processing...')
dataset['blank_lines_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.blank_lines_count(x))
print('Feature 1 done!')

print('Feature 2 processing...')
dataset['blank_spaces_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.blank_spaces_count(x))
print('Feature 2 done!')

print('Feature 3 processing...')
dataset['word_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.word_count(x))
print('Feature 3 done!')

print('Feature 4 processing...')
dataset['average_word_len'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.average_word_len(x))
print('Feature 4 done!')

print('Feature 5 processing...')
dataset['webpage_size'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.webpage_size(x))
print('Feature 5 done!')

print('Feature 6 processing...')
dataset['webpage_entropy'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.webpage_entropy(x))
print('Feature 6 done!')

print('Feature 7 processing...')
dataset['js_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.js_count(x))
print('Feature 7 done!')

print('Feature 8 processing...')
dataset['sus_js_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.sus_js_count(x))
print('Feature 8 done!')

print('Feature 9 processing...')
dataset['js_eval_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.js_eval_count(x))
print('Feature 9 done!')

print('Feature 10 processing...')
dataset['js_escape_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.js_escape_count(x))
print('Feature 10 done!')

print('Feature 11 processing...')
dataset['js_unescape_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.js_unescape_count(x))
print('Feature 11 done!')

print('Feature 12 processing...')
dataset['js_find_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.js_find_count(x))
print('Feature 12 done!')

print('Feature 13 processing...')
dataset['js_exec_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.js_exec_count(x))
print('Feature 13 done!')

print('Feature 14 processing...')
dataset['js_search_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.js_search_count(x))
print('Feature 14 done!')

print('Feature 15 processing...')
dataset['js_link_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.js_link_count(x))
print('Feature 15 done!')

print('Feature 16 processing...')
dataset['js_winopen_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.js_winopen_count(x))
print('Feature 16 done!')

print('Feature 17 processing...')
dataset['title_tag_presence'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.title_tag_presence(x))
print('Feature 17 done!')

print('Feature 18 processing...')
dataset['iframe_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.iframe_count(x))
print('Feature 18 done!')

print('Feature 19 processing...')
dataset['hyperlink_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.hyperlink_count(x))
print('Feature 19 done!')

print('Feature 20 processing...')
dataset['embed_tag_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.embed_tag_count(x))
print('Feature 20 done!')

print('Feature 21 processing...')
dataset['object_tag_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.object_tag_count(x))
print('Feature 21 done!')

print('Feature 22 processing...')
dataset['meta_tag_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.meta_tag_count(x))
print('Feature 22 done!')

print('Feature 23 processing...')
dataset['div_tag_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.div_tag_count(x))
print('Feature 23 done!')

print('Feature 24 processing...')
dataset['body_tag_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.body_tag_count(x))
print('Feature 24 done!')

print('Feature 25 processing...')
dataset['form_tag_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.form_tag_count(x))
print('Feature 25 done!')

print('Feature 26 processing...')
dataset['anchor_tag_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.anchor_tag_count(x))
print('Feature 26 done!')

print('Feature 27 processing...')
dataset['applet_tag_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.applet_tag_count(x))
print('Feature 27 done!')

print('Feature 28 processing...')
dataset['input_tag_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.input_tag_count(x))
print('Feature 28 done!')

print('Feature 29 processing...')
dataset['image_tag_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.image_tag_count(x))
print('Feature 29 done!')

print('Feature 30 processing...')
dataset['span_tag_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.span_tag_count(x))
print('Feature 30 done!')

print('Feature 31 processing...')
dataset['audio_tag_count'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.audio_tag_count(x))
print('Feature 31 done!')

print('Feature 32 processing...')
dataset['has_log_in_html'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.has_log_in_html(x))
print('Feature 32 done!')

print('Feature 33 processing...')
dataset['has_pay_in_html'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.has_pay_in_html(x))
print('Feature 33 done!')

print('Feature 34 processing...')
dataset['has_free_in_html'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.has_free_in_html(x))
print('Feature 34 done!')

print('Feature 35 processing...')
dataset['has_access_in_html'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.has_access_in_html(x))
print('Feature 35 done!')

print('Feature 36 processing...')
dataset['has_bonus_in_html'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.has_bonus_in_html(x))
print('Feature 36 done!')

print('Feature 37 processing...')
dataset['has_click_in_html'] = dataset['html'].apply(lambda x: feature_generation_content_function_htmlin.has_click_in_html(x))
print('Feature 37 done!')

print('Generation time: ', datetime.now() - s)

dataset = dataset.drop(columns = ['url', 'type', 'html'])

print(dataset)

dataset.to_csv("final_unbalanced_with_content.csv", encoding='utf-8', index=False)