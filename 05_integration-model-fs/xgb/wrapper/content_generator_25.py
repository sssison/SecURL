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
        return 0

def get_tld(url):
    tld_lookup = pd.read_csv('tld_lookup.csv')
    parsed_url = urllib.parse.urlparse(url)
    tld = parsed_url.netloc.split('.')[-1].split(':')[0]
    try:
        return tld_lookup[tld].iloc[0]
    except:
        return 0
    
def feature_generator(url):

    html = feature_generation_content_function_htmlin.get_html(url)
    temp = [[url, html]]
    url_test = pd.DataFrame(temp, columns=['url', 'html'])

    url_test['blank_lines_count'] = url_test['html'].apply(lambda x: feature_generation_content_function_htmlin.blank_lines_count(x))

    url_test['word_count'] = url_test['html'].apply(lambda x: feature_generation_content_function_htmlin.word_count(x))

    url_test['js_count'] = url_test['html'].apply(lambda x: feature_generation_content_function_htmlin.js_count(x))

    url_test['js_link_count'] = url_test['html'].apply(lambda x: feature_generation_content_function_htmlin.js_link_count(x))

    url_test['js_winopen_count'] = url_test['html'].apply(lambda x: feature_generation_content_function_htmlin.js_winopen_count(x))

    url_test['meta_tag_count'] = url_test['html'].apply(lambda x: feature_generation_content_function_htmlin.meta_tag_count(x))

    url_test['anchor_tag_count'] = url_test['html'].apply(lambda x: feature_generation_content_function_htmlin.anchor_tag_count(x))

    url_test['input_tag_count'] = url_test['html'].apply(lambda x: feature_generation_content_function_htmlin.input_tag_count(x))

    url_test['has_free_in_html'] = url_test['html'].apply(lambda x: feature_generation_content_function_htmlin.has_free_in_html(x))

    url_test['url_length'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_length(x))

    url_test['url_domain_entropy'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_domain_entropy(x))

    url_test['url_number_of_digits'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_number_of_digits(x))

    url_test['url_path_length'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_path_length(x))

    url_test['url_host_length'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_host_length(x))

    url_test['url_number_of_subdirectories'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_number_of_subdirectories(x))

    url_test['url_has_port'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_has_port(x))

    url_test['url_number_of_fragments'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_number_of_fragments(x))

    url_test['url_num_periods'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_periods(x))

    url_test['has_ebayisapi_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_ebayisapi_in_string(x))

    url_test['has_logon_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_logon_in_string(x))

    url_test['has_signon_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_signon_in_string(x))

    url_test['has_loginasp_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_loginasp_in_string(x))

    url_test['has_exe_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_exe_in_string(x))

    url_test['has_zip_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_zip_in_string(x))

    url_test['has_paypal_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_paypal_in_string(x))

    url_test = url_test.drop(columns=['url', 'html'])

    return url_test
