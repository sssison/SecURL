import pickle
import joblib
import re
import nltk
import tldextract
import hashlib
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from colorama import Fore
from urllib.parse import urlparse
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, classification_report
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, ExtraTreesClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB
from tld import get_tld, is_tld
from tld.exceptions import TldDomainNotFound, TldBadUrl, TldIOError
import logging
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier
import whois
from sklearn.pipeline import Pipeline
from datetime import datetime
from plotly.subplots import make_subplots
from wordcloud import WordCloud
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier, ExtraTreesClassifier, BaggingClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.neural_network import MLPClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans
from sklearn.linear_model import RidgeClassifier, Perceptron, SGDClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time

import feature_generation_lexical_function

def generator(url):

    temp = [[url]]
    url_test = pd.DataFrame(temp, columns=['url'])

    print("First 10 Features")
    print("------------------")
    url_test['url_length'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_length(x))
    print("Feature 1 Done...")

    url_test['url_ip_in_domain'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_ip_in_domain(x))
    print("Feature 2 Done...")

    url_test['url_domain_entropy'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_domain_entropy(x))
    print("Feature 3 Done...")

    url_test['url_is_digits_in_domain'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_is_digits_in_domain(x))
    print("Feature 4 Done...")

    url_test['url_query_length'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_query_length(x))
    print("Feature 5 Done...")

    url_test['url_number_of_parameters'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_number_of_parameters(x))
    print("Feature 6 Done...")

    url_test['url_number_of_digits'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_number_of_digits(x))
    print("Feature 7 Done...")

    url_test['url_string_entropy'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_string_entropy(x))
    print("Feature 8 Done...")

    url_test['url_is_https'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_is_https(x))
    print("Feature 9 Done...")

    url_test['url_path_length'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_path_length(x))
    print("Feature 10 Done...")

    print("Features 11-20")
    print("------------------")
    url_test['url_host_length'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_host_length(x))
    print("Feature 11 Done...")

    url_test['url_number_of_subdirectories'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_number_of_subdirectories(x))
    print("Feature 12 Done...")

    url_test['get_tld'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.get_tld(x))
    print("Feature 13 Done...")

    url_test['url_domain_len'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_domain_len(x))
    print("Feature 14 Done...")

    url_test['url_num_subdomain'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_subdomain(x))
    print("Feature 15 Done...")

    url_test['url_has_port'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_has_port(x))
    print("Feature 16 Done...")

    url_test['url_number_of_fragments'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_number_of_fragments(x))
    print("Feature 17 Done...")

    url_test['url_is_encoded'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_is_encoded(x))
    print("Feature 18 Done...")

    url_test['url_number_of_letters'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_number_of_letters(x))
    print("Feature 19 Done...")

    url_test['url_num_periods'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_periods(x))
    print("Feature 20 Done...")

    print("Features 21-30")
    print("------------------")
    url_test['url_num_of_hyphens'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_of_hyphens(x))
    print("Feature 21 Done...")

    url_test['url_num_underscore'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_underscore(x))
    print("Feature 22 Done...")

    url_test['url_num_equal'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_equal(x))
    print("Feature 23 Done...")

    url_test['url_num_forward_slash'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_forward_slash(x))
    print("Feature 24 Done...")

    url_test['url_num_question_mark'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_question_mark(x))
    print("Feature 25 Done...")

    url_test['url_num_semicolon'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_semicolon(x))
    print("Feature 26 Done...")

    url_test['url_num_open_parenthesis'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_open_parenthesis(x))
    print("Feature 27 Done...")

    url_test['url_num_close_parenthesis'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_close_parenthesis(x))
    print("Feature 28 Done...")

    url_test['url_num_mod_sign'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_mod_sign(x))
    print("Feature 29 Done...")

    url_test['url_num_ampersand'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_ampersand(x))
    print("Feature 30 Done...")

    print("Features 31-40")
    print("------------------")
    url_test['url_num_at'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_at(x))
    print("Feature 31 Done...")

    url_test['has_secure_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_secure_in_string(x))
    print("Feature 32 Done...")

    url_test['has_account_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_account_in_string(x))
    print("Feature 33 Done...")

    url_test['has_webscr_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_webscr_in_string(x))
    print("Feature 34 Done...")

    url_test['has_login_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_login_in_string(x))
    print("Feature 35 Done...")

    url_test['has_ebayisapi_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_ebayisapi_in_string(x))
    print("Feature 36 Done...")

    url_test['has_signin_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_signin_in_string(x))
    print("Feature 37 Done...")

    url_test['has_banking_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_banking_in_string(x))
    print("Feature 38 Done...")

    url_test['has_confirm_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_confirm_in_string(x))
    print("Feature 39 Done...")

    url_test['has_blog_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_blog_in_string(x))
    print("Feature 40 Done...")

    print("Features 41-50")
    print("------------------")
    url_test['has_logon_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_logon_in_string(x))
    print("Feature 41 Done...")

    url_test['has_signon_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_signon_in_string(x))
    print("Feature 42 Done...")

    url_test['has_loginasp_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_loginasp_in_string(x))
    print("Feature 43 Done...")

    url_test['has_loginphp_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_loginphp_in_string(x))
    print("Feature 44 Done...")

    url_test['has_loginhtm_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_loginhtm_in_string(x))
    print("Feature 45 Done...")

    url_test['has_exe_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_exe_in_string(x))
    print("Feature 46 Done...")

    url_test['has_zip_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_zip_in_string(x))
    print("Feature 47 Done...")

    url_test['has_rar_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_rar_in_string(x))
    print("Feature 48 Done...")

    url_test['has_jpg_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_jpg_in_string(x))
    print("Feature 49 Done...")

    url_test['has_gif_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_gif_in_string(x))
    print("Feature 50 Done...")

    print("Features 51-60")
    print("------------------")
    url_test['has_viewerphp_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_viewerphp_in_string(x))
    print("Feature 51 Done...")

    url_test['has_linkeq_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_linkeq_in_string(x))
    print("Feature 52 Done...")

    url_test['has_getImageasp_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_getImageasp_in_string(x))
    print("Feature 53 Done...")

    url_test['has_plugins_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_plugins_in_string(x))
    print("Feature 54 Done...")

    url_test['has_paypal_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_paypal_in_string(x))
    print("Feature 55 Done...")

    url_test['has_order_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_order_in_string(x))
    print("Feature 56 Done...")

    url_test['has_dbsysphp_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_dbsysphp_in_string(x))
    print("Feature 57 Done...")

    url_test['has_configbin_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_configbin_in_string(x))
    print("Feature 58 Done...")

    url_test['has_downloadphp_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_downloadphp_in_string(x))
    print("Feature 59 Done...")

    url_test['has_js_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_js_in_string(x))
    print("Feature 60 Done...")

    print("Features 61-70")
    print("------------------")
    url_test['has_payment_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_payment_in_string(x))
    print("Feature 61 Done...")

    url_test['has_files_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_files_in_string(x))
    print("Feature 62 Done...")

    url_test['has_css_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_css_in_string(x))
    print("Feature 63 Done...")

    url_test['has_shopping_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_shopping_in_string(x))
    print("Feature 64 Done...")

    url_test['has_mailphp_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_mailphp_in_string(x))
    print("Feature 65 Done...")

    url_test['has_jar_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_jar_in_string(x))
    print("Feature 66 Done...")

    url_test['has_swf_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_swf_in_string(x))
    print("Feature 67 Done...")

    url_test['has_cgi_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_cgi_in_string(x))
    print("Feature 68 Done...")

    url_test['has_php_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_php_in_string(x))
    print("Feature 69 Done...")

    url_test['has_abuse_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_abuse_in_string(x))
    print("Feature 70 Done...")

    print("Features 71-75")
    print("------------------")
    url_test['has_admin_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_admin_in_string(x))
    print("Feature 71 Done...")

    url_test['has_bin_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_bin_in_string(x))
    print("Feature 72 Done...")

    url_test['has_personal_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_personal_in_string(x))
    print("Feature 73 Done...")

    url_test['has_update_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_update_in_string(x))
    print("Feature 74 Done...")

    url_test['has_verification_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_verification_in_string(x))
    print("Feature 75 Done...")

    url_test = url_test.drop(columns=['url'])

    return url_test

from xgboost import XGBClassifier, DMatrix, train
from lexical_generator_33 import lexical_generator

def predict_maliciousness(url):

    pipeline = joblib.load("model/xgb_wrapper_33_lexical.sav")

    numerical_values = lexical_generator(url)

    numerical_values = DMatrix(numerical_values)

    match pipeline.predict(numerical_values):
        case 0:
            return "Benign"
        case 1:
            return "Malware"