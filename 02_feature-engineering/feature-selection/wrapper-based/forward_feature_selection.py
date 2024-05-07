import pandas as pd
from mlxtend.feature_selection import SequentialFeatureSelector
from xgboost import XGBClassifier
import feature_generation_lexical_function as fgl
from sklearn.preprocessing import LabelEncoder

def lexical_generation(dataset):
    print('Generating lexical features...')

    dataset['url_length'] = dataset['url'].apply(lambda x: fgl.url_length(x))

    dataset['url_ip_in_domain'] = dataset['url'].apply(lambda x: fgl.url_ip_in_domain(x))

    dataset['url_domain_entropy'] = dataset['url'].apply(lambda x: fgl.url_domain_entropy(x))

    dataset['url_is_digits_in_domain'] = dataset['url'].apply(lambda x: fgl.url_is_digits_in_domain(x))

    dataset['url_query_length'] = dataset['url'].apply(lambda x: fgl.url_query_length(x))

    dataset['url_number_of_parameters'] = dataset['url'].apply(lambda x: fgl.url_number_of_parameters(x))

    dataset['url_number_of_digits'] = dataset['url'].apply(lambda x: fgl.url_number_of_digits(x))

    dataset['url_string_entropy'] = dataset['url'].apply(lambda x: fgl.url_string_entropy(x))

    dataset['url_is_https'] = dataset['url'].apply(lambda x: fgl.url_is_https(x))

    dataset['url_path_length'] = dataset['url'].apply(lambda x: fgl.url_path_length(x))

    dataset['url_host_length'] = dataset['url'].apply(lambda x: fgl.url_host_length(x))

    dataset['url_number_of_subdirectories'] = dataset['url'].apply(lambda x: fgl.url_number_of_subdirectories(x))

    dataset['get_tld'] = dataset['url'].apply(lambda x: fgl.get_tld(x))

    dataset['url_domain_len'] = dataset['url'].apply(lambda x: fgl.url_domain_len(x))

    dataset['url_num_subdomain'] = dataset['url'].apply(lambda x: fgl.url_num_subdomain(x))

    dataset['url_has_port'] = dataset['url'].apply(lambda x: fgl.url_has_port(x))

    dataset['url_number_of_fragments'] = dataset['url'].apply(lambda x: fgl.url_number_of_fragments(x))

    dataset['url_is_encoded'] = dataset['url'].apply(lambda x: fgl.url_is_encoded(x))

    dataset['url_number_of_letters'] = dataset['url'].apply(lambda x: fgl.url_number_of_letters(x))

    dataset['url_num_periods'] = dataset['url'].apply(lambda x: fgl.url_num_periods(x))

    dataset['url_num_of_hyphens'] = dataset['url'].apply(lambda x: fgl.url_num_of_hyphens(x))

    dataset['url_num_underscore'] = dataset['url'].apply(lambda x: fgl.url_num_underscore(x))

    dataset['url_num_equal'] = dataset['url'].apply(lambda x: fgl.url_num_equal(x))

    dataset['url_num_forward_slash'] = dataset['url'].apply(lambda x: fgl.url_num_forward_slash(x))

    dataset['url_num_question_mark'] = dataset['url'].apply(lambda x: fgl.url_num_question_mark(x))

    dataset['url_num_semicolon'] = dataset['url'].apply(lambda x: fgl.url_num_semicolon(x))

    dataset['url_num_open_parenthesis'] = dataset['url'].apply(lambda x: fgl.url_num_open_parenthesis(x))

    dataset['url_num_close_parenthesis'] = dataset['url'].apply(lambda x: fgl.url_num_close_parenthesis(x))

    dataset['url_num_mod_sign'] = dataset['url'].apply(lambda x: fgl.url_num_mod_sign(x))

    dataset['url_num_ampersand'] = dataset['url'].apply(lambda x: fgl.url_num_ampersand(x))

    dataset['url_num_at'] = dataset['url'].apply(lambda x: fgl.url_num_at(x))

    dataset['has_secure_in_string'] = dataset['url'].apply(lambda x: fgl.has_secure_in_string(x))

    dataset['has_account_in_string'] = dataset['url'].apply(lambda x: fgl.has_account_in_string(x))

    dataset['has_webscr_in_string'] = dataset['url'].apply(lambda x: fgl.has_webscr_in_string(x))

    dataset['has_login_in_string'] = dataset['url'].apply(lambda x: fgl.has_login_in_string(x))

    dataset['has_ebayisapi_in_string'] = dataset['url'].apply(lambda x: fgl.has_ebayisapi_in_string(x))

    dataset['has_signin_in_string'] = dataset['url'].apply(lambda x: fgl.has_signin_in_string(x))

    dataset['has_banking_in_string'] = dataset['url'].apply(lambda x: fgl.has_banking_in_string(x))

    dataset['has_confirm_in_string'] = dataset['url'].apply(lambda x: fgl.has_confirm_in_string(x))

    dataset['has_blog_in_string'] = dataset['url'].apply(lambda x: fgl.has_blog_in_string(x))

    dataset['has_logon_in_string'] = dataset['url'].apply(lambda x: fgl.has_logon_in_string(x))

    dataset['has_signon_in_string'] = dataset['url'].apply(lambda x: fgl.has_signon_in_string(x))

    dataset['has_loginasp_in_string'] = dataset['url'].apply(lambda x: fgl.has_loginasp_in_string(x))

    dataset['has_loginphp_in_string'] = dataset['url'].apply(lambda x: fgl.has_loginphp_in_string(x))

    dataset['has_loginhtm_in_string'] = dataset['url'].apply(lambda x: fgl.has_loginhtm_in_string(x))

    dataset['has_exe_in_string'] = dataset['url'].apply(lambda x: fgl.has_exe_in_string(x))

    dataset['has_zip_in_string'] = dataset['url'].apply(lambda x: fgl.has_zip_in_string(x))

    dataset['has_rar_in_string'] = dataset['url'].apply(lambda x: fgl.has_rar_in_string(x))

    dataset['has_jpg_in_string'] = dataset['url'].apply(lambda x: fgl.has_jpg_in_string(x))

    dataset['has_gif_in_string'] = dataset['url'].apply(lambda x: fgl.has_gif_in_string(x))

    dataset['has_viewerphp_in_string'] = dataset['url'].apply(lambda x: fgl.has_viewerphp_in_string(x))

    dataset['has_linkeq_in_string'] = dataset['url'].apply(lambda x: fgl.has_linkeq_in_string(x))

    dataset['has_getImageasp_in_string'] = dataset['url'].apply(lambda x: fgl.has_getImageasp_in_string(x))

    dataset['has_plugins_in_string'] = dataset['url'].apply(lambda x: fgl.has_plugins_in_string(x))

    dataset['has_paypal_in_string'] = dataset['url'].apply(lambda x: fgl.has_paypal_in_string(x))

    dataset['has_order_in_string'] = dataset['url'].apply(lambda x: fgl.has_order_in_string(x))

    dataset['has_dbsysphp_in_string'] = dataset['url'].apply(lambda x: fgl.has_dbsysphp_in_string(x))

    dataset['has_configbin_in_string'] = dataset['url'].apply(lambda x: fgl.has_configbin_in_string(x))

    dataset['has_downloadphp_in_string'] = dataset['url'].apply(lambda x: fgl.has_downloadphp_in_string(x))

    dataset['has_js_in_string'] = dataset['url'].apply(lambda x: fgl.has_js_in_string(x))

    dataset['has_payment_in_string'] = dataset['url'].apply(lambda x: fgl.has_payment_in_string(x))

    dataset['has_files_in_string'] = dataset['url'].apply(lambda x: fgl.has_files_in_string(x))

    dataset['has_css_in_string'] = dataset['url'].apply(lambda x: fgl.has_css_in_string(x))

    dataset['has_shopping_in_string'] = dataset['url'].apply(lambda x: fgl.has_shopping_in_string(x))

    dataset['has_mailphp_in_string'] = dataset['url'].apply(lambda x: fgl.has_mailphp_in_string(x))

    dataset['has_jar_in_string'] = dataset['url'].apply(lambda x: fgl.has_jar_in_string(x))

    dataset['has_swf_in_string'] = dataset['url'].apply(lambda x: fgl.has_swf_in_string(x))

    dataset['has_cgi_in_string'] = dataset['url'].apply(lambda x: fgl.has_cgi_in_string(x))

    dataset['has_php_in_string'] = dataset['url'].apply(lambda x: fgl.has_php_in_string(x))

    dataset['has_abuse_in_string'] = dataset['url'].apply(lambda x: fgl.has_abuse_in_string(x))

    dataset['has_admin_in_string'] = dataset['url'].apply(lambda x: fgl.has_admin_in_string(x))

    dataset['has_bin_in_string'] = dataset['url'].apply(lambda x: fgl.has_bin_in_string(x))

    dataset['has_personal_in_string'] = dataset['url'].apply(lambda x: fgl.has_personal_in_string(x))

    dataset['has_update_in_string'] = dataset['url'].apply(lambda x: fgl.has_update_in_string(x))

    dataset['has_verification_in_string'] = dataset['url'].apply(lambda x: fgl.has_verification_in_string(x))

    dataset['url_scheme'] = dataset['url'].apply(lambda x: fgl.url_scheme(x))

    print('Lexical features have been generated.')

    print('Removing duplicates...')
    dataset.drop_duplicates(inplace = True, keep='first')
    print('Duplicates removed.')

    print('Applying label encoding...')
    get_tld = dataset['get_tld'].to_list()
    url_scheme = dataset['url_scheme'].to_list()

    le = LabelEncoder()
    dataset['get_tld'] = le.fit_transform(dataset['get_tld'])
    dataset['url_scheme'] = le.fit_transform(dataset['url_scheme'])

    scheme_cat = dataset['url_scheme'].to_list()
    tld_cat = dataset['get_tld'].to_list()
    print('Label encoding applied.')

    print('Creating categorical lookup table...')
    scheme_lookup = {}
    tld_lookup = {}

    i = 0
    for scheme in url_scheme:
        scheme_lookup[scheme] = scheme_cat[i]
        i += 1
    i = 0
    scheme_lookup_pd = pd.DataFrame([scheme_lookup])
    scheme_lookup_pd.to_csv("scheme_lookup.csv", encoding='utf-8', index=False)

    for tld in get_tld:
        tld_lookup [tld] = tld_cat[i]
        i += 1
    tld_lookup_pd = pd.DataFrame([tld_lookup])
    tld_lookup_pd.to_csv("tld_lookup.csv", encoding='utf-8', index=False)
    print('Lookup table has been generated.')

    return dataset
    
def content_generation(url_dataset):
#insert feature dataset generation here

def xgb_ffs(dataset_with_feature_csv):
    dataset = pd.read_csv(dataset_with_feature_csv)
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