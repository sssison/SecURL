import pandas as pd                     # For data transformation
import numpy as numpy                   # For scientific calculations
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, classification_report
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, ConfusionMatrixDisplay
from xgboost import XGBClassifier, DMatrix, train
from sklearn.pipeline import Pipeline
import time
from datetime import datetime
import joblib
import os
import optuna
from sklearn.metrics import mean_squared_error # or any other metric
from sklearn.model_selection import train_test_split
import machine_learning
import database_operations
import feature_engineering


temp_list_lexical = ['url_length',
                        'url_domain_entropy',
                        'url_is_digits_in_domain',
                        'url_number_of_parameters',
                        'url_number_of_digits',
                        'url_string_entropy',
                        'url_path_length',
                        'url_host_length',
                        'get_tld',
                        'url_domain_len',
                        'url_num_subdomain',
                        'url_number_of_fragments',
                        'url_is_encoded',
                        'url_number_of_letters',
                        'url_num_periods',
                        'url_num_of_hyphens',
                        'url_num_underscore',
                        'url_num_forward_slash',
                        'url_num_semicolon',
                        'url_num_mod_sign',
                        'has_login_in_string',
                        'has_signin_in_string',
                        'has_logon_in_string',
                        'has_loginasp_in_string',
                        'has_exe_in_string',
                        'has_viewerphp_in_string',
                        'has_getImageasp_in_string',
                        'has_paypal_in_string',
                        'has_dbsysphp_in_string',
                        'has_shopping_in_string',
                        'has_php_in_string',
                        'has_bin_in_string',
                        'has_personal_in_string',
                        'url_scheme'
                        ]
    
temp_list_content = ['blank_lines_count', 
                    'word_count', 
                    'js_count', 
                    'js_find_count', 
                    'js_link_count', 
                    'js_winopen_count', 
                    'title_tag_presence', 
                    'meta_tag_count', 
                    'anchor_tag_count', 
                    'applet_tag_count', 
                    'input_tag_count', 
                    'has_free_in_html', 
                    'has_access_in_html', 
                    'url_length', 
                    'url_ip_in_domain', 
                    'url_domain_entropy', 
                    'url_is_digits_in_domain', 
                    'url_number_of_digits', 
                    'url_string_entropy', 
                    'url_path_length', 
                    'url_host_length', 
                    'url_number_of_subdirectories', 
                    'url_num_subdomain', 
                    'url_has_port', 
                    'url_number_of_fragments', 
                    'url_num_periods', 
                    'url_num_equal', 
                    'url_num_open_parenthesis', 
                    'url_num_close_parenthesis', 
                    'url_num_ampersand', 
                    'url_num_at', 
                    'has_account_in_string', 
                    'has_webscr_in_string', 
                    'has_ebayisapi_in_string', 
                    'has_signin_in_string', 
                    'has_banking_in_string', 
                    'has_confirm_in_string', 
                    'has_logon_in_string', 
                    'has_signon_in_string', 
                    'has_loginasp_in_string', 
                    'has_loginphp_in_string', 
                    'has_exe_in_string', 
                    'has_zip_in_string', 
                    'has_rar_in_string', 
                    'has_jpg_in_string', 
                    'has_gif_in_string', 
                    'has_viewerphp_in_string', 
                    'has_getImageasp_in_string', 
                    'has_plugins_in_string', 
                    'has_paypal_in_string', 
                    'has_dbsysphp_in_string', 
                    'has_configbin_in_string', 
                    'has_downloadphp_in_string', 
                    'has_payment_in_string', 
                    'has_files_in_string', 
                    'has_shopping_in_string', 
                    'has_mailphp_in_string', 
                    'has_jar_in_string', 
                    'has_swf_in_string', 
                    'has_cgi_in_string', 
                    'has_php_in_string', 
                    'has_abuse_in_string', 
                    'has_bin_in_string', 
                    'has_update_in_string', 
                    'has_verification_in_string']

def async_call():

    # Reads training csv
    warm_up_actual = pd.read_csv("databases/warm-up-actual.csv")
    warm_up_predicted = pd.read_csv("databases/warm-up-predicted.csv")

    # Reads from current database
    # test_actual = database_operations.column_to_pd("databases/securl_transactions.db", "actual")
    # test_predicted = database_operations.column_to_pd("databases/securl_transactions.db", "prediction")

    # For Testing purposes
    test_actual = pd.read_csv("databases/testing-actual.csv")
    test_predicted = pd.read_csv("databases/testing-predicted.csv")

    is_conceptDrift = machine_learning.concept_drift_detector(warm_up_predicted, warm_up_actual, test_predicted, test_actual)

    if (is_conceptDrift):
        
        print("I'm Retraining!")

        legacy_data_lexical = pd.read_csv("databases/legacy_dataset_lexical.csv")
        legacy_data_lexical_content = pd.read_csv("databases/legacy_dataset_lexical-content.csv")

        new_data_lexical = database_operations.column_to_pd("databases/securl_transactions.db", "url, actual")
        new_data_lexical['url_type'] = new_data_lexical['actual']
        new_data_lexical = new_data_lexical.drop(columns = ['actual'])
        new_data_lexical = feature_engineering.lexical_generation(new_data_lexical)

        new_data_lexical_content = feature_engineering.content_generation(new_data_lexical)

        new_data_lexical = new_data_lexical.drop(columns=['url'])
        new_data_lexical_content = new_data_lexical_content.drop(columns=['url'])

        retrain_dataset_lexical = pd.concat([legacy_data_lexical, new_data_lexical])
        retrain_dataset_lexical_content = pd.concat([legacy_data_lexical_content, new_data_lexical_content])

        print(retrain_dataset_lexical.head())
        print(retrain_dataset_lexical_content.head())

        X_train_lexical, X_test_lexical, y_train_lexical, y_test_lexical = train_test_split(retrain_dataset_lexical.drop(columns=['url_type']), retrain_dataset_lexical['url_type'], test_size = 0.2, random_state=42)
        X_train_lexical_content, X_test_lexical_content, y_train_lexical_content, y_test_lexical_content = train_test_split(retrain_dataset_lexical_content.drop(columns=['url_type']), retrain_dataset_lexical_content['url_type'], test_size = 0.2, random_state=42)

        X_train_lexical = X_train_lexical[temp_list_lexical]
        X_test_lexical = X_test_lexical[temp_list_lexical]

        X_train_lexical_content = X_train_lexical_content[temp_list_content]
        X_test_lexical_content = X_test_lexical_content[temp_list_content]

        # parameters_lexical = machine_learning.hyperparameter_tuning(X_train_lexical, y_train_lexical)
        # parameters_lexical_content = machine_learning.hyperparameter_tuning(X_train_lexical_content, y_train_lexical_content)

        print("Starting re-training...")

        # machine_learning.model_training(X_train_lexical, y_train_lexical, X_test_lexical, y_test_lexical, parameters_lexical, "model/xgb-lexical-test.sav")
        # machine_learning.model_training(X_train_lexical_content, y_train_lexical_content, X_test_lexical_content, y_test_lexical_content, parameters_lexical_content, "model/xgb-lexical-content-test.sav")

        print("Retraining finished!")

    else:
        print("Wala pa, wag excited!")
        return 

async_call()