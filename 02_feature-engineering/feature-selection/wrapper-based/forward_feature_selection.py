import pandas as pd
from mlxtend.feature_selection import SequentialFeatureSelector
from xgboost import XGBClassifier
import feature_generation_lexical_function as fgl
import feature_generation_content_function_htmlin as fgc
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

    print('Removing null data...')
    dataset = dataset.dropna()
    print('Null data has been removed.')

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
    
def content_generation(dataset):
    print('Generating content-based features...')

    dataset['blank_lines_count'] = None
    dataset['blank_spaces_count'] = None
    dataset['word_count'] = None
    dataset['average_word_len'] = None
    dataset['webpage_size'] = None
    dataset['webpage_entropy'] = None
    dataset['js_count'] = None
    dataset['sus_js_count'] = None
    dataset['js_eval_count'] = None
    dataset['js_escape_count'] = None
    dataset['js_unescape_count'] = None
    dataset['js_find_count'] = None
    dataset['js_exec_count'] = None
    dataset['js_search_count'] = None
    dataset['js_link_count'] = None
    dataset['js_winopen_count'] = None
    dataset['title_tag_presence'] = None
    dataset['iframe_count'] = None
    dataset['hyperlink_count'] = None
    dataset['embed_tag_count'] = None
    dataset['object_tag_count'] = None
    dataset['meta_tag_count'] = None
    dataset['div_tag_count'] = None
    dataset['body_tag_count'] = None
    dataset['form_tag_count'] = None
    dataset['anchor_tag_count'] = None
    dataset['applet_tag_count'] = None
    dataset['input_tag_count'] = None
    dataset['image_tag_count'] = None
    dataset['span_tag_count'] = None
    dataset['audio_tag_count'] = None
    dataset['has_log_in_html'] = None
    dataset['has_pay_in_html'] = None
    dataset['has_free_in_html'] = None
    dataset['has_access_in_html'] = None
    dataset['has_bonus_in_html'] = None
    dataset['has_click_in_html'] = None

    for i in range(len(dataset.index)):
        url = dataset.iloc[i]['url']
        html = fgc.get_html(url)

        dataset['blank_lines_count'][i] = fgc.blank_lines_count(html)

        dataset['blank_spaces_count'][i] = fgc.blank_spaces_count(html)

        dataset['word_count'][i] = fgc.word_count(html)

        dataset['average_word_len'][i] = fgc.average_word_len(html)

        dataset['webpage_size'][i] = fgc.webpage_size(html)

        dataset['webpage_entropy'][i] = fgc.webpage_entropy(html)

        dataset['js_count'][i] = fgc.js_count(html)

        dataset['sus_js_count'][i] = fgc.sus_js_count(html)

        dataset['js_eval_count'][i] = fgc.js_eval_count(html)

        dataset['js_escape_count'][i] = fgc.js_escape_count(html)

        dataset['js_unescape_count'][i] = fgc.js_unescape_count(html)

        dataset['js_find_count'][i] = fgc.js_find_count(html)

        dataset['js_exec_count'][i] = fgc.js_exec_count(html)

        dataset['js_search_count'][i] = fgc.js_search_count(html)

        dataset['js_link_count'][i] = fgc.js_link_count(html)

        dataset['js_winopen_count'][i] = fgc.js_winopen_count(html)

        dataset['title_tag_presence'][i] = fgc.title_tag_presence(html)

        dataset['iframe_count'][i] = fgc.iframe_count(html)

        dataset['hyperlink_count'][i] = fgc.hyperlink_count(html)

        dataset['embed_tag_count'][i] = fgc.embed_tag_count(html)

        dataset['object_tag_count'][i] = fgc.object_tag_count(html)

        dataset['meta_tag_count'][i] = fgc.meta_tag_count(html)

        dataset['div_tag_count'][i] = fgc.div_tag_count(html)

        dataset['body_tag_count'][i] = fgc.body_tag_count(html)

        dataset['form_tag_count'][i] = fgc.form_tag_count(html)

        dataset['anchor_tag_count'][i] = fgc.anchor_tag_count(html)

        dataset['applet_tag_count'][i] = fgc.applet_tag_count(html)

        dataset['input_tag_count'][i] = fgc.input_tag_count(html)

        dataset['image_tag_count'][i] = fgc.image_tag_count(html)

        dataset['span_tag_count'][i] = fgc.span_tag_count(html)

        dataset['audio_tag_count'][i] = fgc.audio_tag_count(html)

        dataset['has_log_in_html'][i] = fgc.has_log_in_html(html)

        dataset['has_pay_in_html'][i] = fgc.has_pay_in_html(html)

        dataset['has_free_in_html'][i] = fgc.has_free_in_html(html)

        dataset['has_access_in_html'][i] = fgc.has_access_in_html(html)

        dataset['has_bonus_in_html'][i] = fgc.has_bonus_in_html(html)

        dataset['has_click_in_html'][i] = fgc.has_click_in_html(html)
    
    print('Content-based features have been genrated.')

    print('Removing duplicates...')
    dataset.drop_duplicates(inplace = True, keep='first')
    print('Duplicates removed.')

    print('Removing null data...')
    dataset = dataset.dropna()
    print('Null data has been removed.')

    return dataset

def xgb_ffs(dataset_with_feature_csv):
    dataset = pd.read_csv(dataset_with_feature_csv)
    # make sure 'url' and 'type' columns have been dropped
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