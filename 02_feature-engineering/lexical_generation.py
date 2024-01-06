import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import feature_generation_lexical_function

dataset = pd.read_csv("final_unbalanced_noFeatures.csv")

dataset["url_type"] = dataset["type"].replace({
    'benign':0,
    'defacement':1,
    'phishing':2,
    'malware':3,
});

print("First 10 Features")
print("------------------")
dataset['url_length'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_length(x))
print("Feature 1 Done...")

dataset['url_ip_in_domain'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_ip_in_domain(x))
print("Feature 2 Done...")

dataset['url_domain_entropy'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_domain_entropy(x))
print("Feature 3 Done...")

dataset['url_is_digits_in_domain'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_is_digits_in_domain(x))
print("Feature 4 Done...")

dataset['url_query_length'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_query_length(x))
print("Feature 5 Done...")

dataset['url_number_of_parameters'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_number_of_parameters(x))
print("Feature 6 Done...")

dataset['url_number_of_digits'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_number_of_digits(x))
print("Feature 7 Done...")

dataset['url_string_entropy'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_string_entropy(x))
print("Feature 8 Done...")

dataset['url_is_https'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_is_https(x))
print("Feature 9 Done...")

dataset['url_path_length'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_path_length(x))
print("Feature 10 Done...")

print("Features 11-20")
print("------------------")
dataset['url_host_length'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_host_length(x))
print("Feature 11 Done...")

dataset['url_number_of_subdirectories'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_number_of_subdirectories(x))
print("Feature 12 Done...")

dataset['get_tld'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.get_tld(x))
print("Feature 13 Done...")

dataset['url_domain_len'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_domain_len(x))
print("Feature 14 Done...")

dataset['url_num_subdomain'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_num_subdomain(x))
print("Feature 15 Done...")

dataset['url_has_port'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_has_port(x))
print("Feature 16 Done...")

dataset['url_number_of_fragments'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_number_of_fragments(x))
print("Feature 17 Done...")

dataset['url_is_encoded'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_is_encoded(x))
print("Feature 18 Done...")

dataset['url_number_of_letters'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_number_of_letters(x))
print("Feature 19 Done...")

dataset['url_num_periods'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_num_periods(x))
print("Feature 20 Done...")

print("Features 21-30")
print("------------------")
dataset['url_num_of_hyphens'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_num_of_hyphens(x))
print("Feature 21 Done...")

dataset['url_num_underscore'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_num_underscore(x))
print("Feature 22 Done...")

dataset['url_num_equal'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_num_equal(x))
print("Feature 23 Done...")

dataset['url_num_forward_slash'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_num_forward_slash(x))
print("Feature 24 Done...")

dataset['url_num_question_mark'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_num_question_mark(x))
print("Feature 25 Done...")

dataset['url_num_semicolon'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_num_semicolon(x))
print("Feature 26 Done...")

dataset['url_num_open_parenthesis'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_num_open_parenthesis(x))
print("Feature 27 Done...")

dataset['url_num_close_parenthesis'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_num_close_parenthesis(x))
print("Feature 28 Done...")

dataset['url_num_mod_sign'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_num_mod_sign(x))
print("Feature 29 Done...")

dataset['url_num_ampersand'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_num_ampersand(x))
print("Feature 30 Done...")

print("Features 31-40")
print("------------------")
dataset['url_num_at'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.url_num_at(x))
print("Feature 31 Done...")

dataset['has_secure_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_secure_in_string(x))
print("Feature 32 Done...")

dataset['has_account_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_account_in_string(x))
print("Feature 33 Done...")

dataset['has_webscr_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_webscr_in_string(x))
print("Feature 34 Done...")

dataset['has_login_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_login_in_string(x))
print("Feature 35 Done...")

dataset['has_ebayisapi_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_ebayisapi_in_string(x))
print("Feature 36 Done...")

dataset['has_signin_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_signin_in_string(x))
print("Feature 37 Done...")

dataset['has_banking_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_banking_in_string(x))
print("Feature 38 Done...")

dataset['has_confirm_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_confirm_in_string(x))
print("Feature 39 Done...")

dataset['has_blog_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_blog_in_string(x))
print("Feature 40 Done...")

print("Features 41-50")
print("------------------")
dataset['has_logon_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_logon_in_string(x))
print("Feature 41 Done...")

dataset['has_signon_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_signon_in_string(x))
print("Feature 42 Done...")

dataset['has_loginasp_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_loginasp_in_string(x))
print("Feature 43 Done...")

dataset['has_loginphp_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_loginphp_in_string(x))
print("Feature 44 Done...")

dataset['has_loginhtm_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_loginhtm_in_string(x))
print("Feature 45 Done...")

dataset['has_exe_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_exe_in_string(x))
print("Feature 46 Done...")

dataset['has_zip_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_zip_in_string(x))
print("Feature 47 Done...")

dataset['has_rar_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_rar_in_string(x))
print("Feature 48 Done...")

dataset['has_jpg_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_jpg_in_string(x))
print("Feature 49 Done...")

dataset['has_gif_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_gif_in_string(x))
print("Feature 50 Done...")

print("Features 51-60")
print("------------------")
dataset['has_viewerphp_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_viewerphp_in_string(x))
print("Feature 51 Done...")

dataset['has_linkeq_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_linkeq_in_string(x))
print("Feature 52 Done...")

dataset['has_getImageasp_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_getImageasp_in_string(x))
print("Feature 53 Done...")

dataset['has_plugins_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_plugins_in_string(x))
print("Feature 54 Done...")

dataset['has_paypal_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_paypal_in_string(x))
print("Feature 55 Done...")

dataset['has_order_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_order_in_string(x))
print("Feature 56 Done...")

dataset['has_dbsysphp_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_dbsysphp_in_string(x))
print("Feature 57 Done...")

dataset['has_configbin_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_configbin_in_string(x))
print("Feature 58 Done...")

dataset['has_downloadphp_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_downloadphp_in_string(x))
print("Feature 59 Done...")

dataset['has_js_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_js_in_string(x))
print("Feature 60 Done...")

print("Features 61-70")
print("------------------")
dataset['has_payment_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_payment_in_string(x))
print("Feature 61 Done...")

dataset['has_files_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_files_in_string(x))
print("Feature 62 Done...")

dataset['has_css_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_css_in_string(x))
print("Feature 63 Done...")

dataset['has_shopping_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_shopping_in_string(x))
print("Feature 64 Done...")

dataset['has_mailphp_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_mailphp_in_string(x))
print("Feature 65 Done...")

dataset['has_jar_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_jar_in_string(x))
print("Feature 66 Done...")

dataset['has_swf_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_swf_in_string(x))
print("Feature 67 Done...")

dataset['has_cgi_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_cgi_in_string(x))
print("Feature 68 Done...")

dataset['has_php_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_php_in_string(x))
print("Feature 69 Done...")

dataset['has_abuse_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_abuse_in_string(x))
print("Feature 70 Done...")

print("Features 71-75")
print("------------------")
dataset['has_admin_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_admin_in_string(x))
print("Feature 71 Done...")

dataset['has_bin_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_bin_in_string(x))
print("Feature 72 Done...")

dataset['has_personal_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_personal_in_string(x))
print("Feature 73 Done...")

dataset['has_update_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_update_in_string(x))
print("Feature 74 Done...")

dataset['has_verification_in_string'] = dataset['url'].apply(lambda x: feature_generation_lexical_function.has_verification_in_string(x))
print("Feature 75 Done...")

print("Removing Duplicates")
dataset.drop_duplicates(inplace = True, keep='first')

print(dataset['type'].value_counts())

# Dropping type and url
dataset = dataset.drop(columns = ['url', 'type'])


dataset.to_csv("final_unbalanced_withLexical.csv", encoding='utf-8', index=False)
dataset.to_csv("../03_machine-learning-model/final_unbalanced_withLexical.csv", encoding='utf-8', index=False)