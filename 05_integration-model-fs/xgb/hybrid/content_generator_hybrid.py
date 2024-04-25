import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import feature_generation_content_function_htmlin
from datetime import datetime
import feature_generation_lexical_function
from sklearn.preprocessing import LabelEncoder
import urllib

def url_scheme(url):
    scheme_lookup = pd.read_csv('scheme_lookup.csv')
    parsed_url = urllib.parse.urlparse(url)
    parsed_url_scheme = parsed_url.scheme
    try:
        return scheme_lookup[parsed_url_scheme].iloc[0]
    except:
        return 999999

def get_tld(url):
    tld_lookup = pd.read_csv('tld_lookup.csv')
    parsed_url = urllib.parse.urlparse(url)
    tld = parsed_url.netloc.split('.')[-1].split(':')[0]
    try:
        return tld_lookup[tld].iloc[0]
    except:
        return 999999
    
def feature_generator(url):

    html = feature_generation_content_function_htmlin.get_html(url)
    temp = [[url, html]]
    url_test = pd.DataFrame(temp, columns=['url', 'html'])

    url_test['webpage_entropy'] = url_test['html'].apply(lambda x: feature_generation_content_function_htmlin.webpage_entropy(x))

    url_test['js_count'] = url_test['html'].apply(lambda x: feature_generation_content_function_htmlin.js_count(x))

    url_test['js_search_count'] = url_test['html'].apply(lambda x: feature_generation_content_function_htmlin.js_search_count(x))

    url_test['meta_tag_count'] = url_test['html'].apply(lambda x: feature_generation_content_function_htmlin.meta_tag_count(x))

    url_test['has_log_in_html'] = url_test['html'].apply(lambda x: feature_generation_content_function_htmlin.has_log_in_html(x))

    url_test['url_query_length'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_query_length(x))

    url_test['url_path_length'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_path_length(x))

    url_test['url_host_length'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_host_length(x))

    url_test['url_num_subdomain'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_subdomain(x))

    url_test['url_num_periods'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_periods(x))

    url_test['url_num_forward_slash'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_forward_slash(x))

    url_test = url_test.drop(columns=['url', 'html'])

    return url_test
