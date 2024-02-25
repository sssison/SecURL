import pandas as pd                     # For data transformation
import feature_generation_lexical_function

def lexical_generator(url):

    temp = [[url]]
    url_test = pd.DataFrame(temp, columns=['url'])

    url_test['url_length'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_length(x))

    url_test['url_ip_in_domain'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_ip_in_domain(x))

    url_test['url_domain_entropy'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_domain_entropy(x))

    url_test['url_is_digits_in_domain'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_is_digits_in_domain(x))

    url_test['url_query_length'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_query_length(x))

    url_test['url_number_of_parameters'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_number_of_parameters(x))

    url_test['url_number_of_digits'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_number_of_digits(x))

    url_test['url_string_entropy'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_string_entropy(x))

    url_test['url_is_https'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_is_https(x))

    url_test['url_path_length'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_path_length(x))

    url_test['url_host_length'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_host_length(x))

    url_test['url_number_of_subdirectories'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_number_of_subdirectories(x))

    url_test['get_tld'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.get_tld(x))

    url_test['url_domain_len'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_domain_len(x))

    url_test['url_num_subdomain'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_subdomain(x))

    url_test['url_has_port'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_has_port(x))

    url_test['url_number_of_fragments'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_number_of_fragments(x))

    url_test['url_is_encoded'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_is_encoded(x))

    url_test['url_number_of_letters'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_number_of_letters(x))

    url_test['url_num_periods'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_periods(x))

    url_test['url_num_of_hyphens'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_of_hyphens(x))

    url_test['url_num_underscore'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_underscore(x))

    url_test['url_num_equal'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_equal(x))

    url_test['url_num_forward_slash'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_forward_slash(x))

    url_test['url_num_question_mark'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_question_mark(x))

    url_test['url_num_semicolon'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_semicolon(x))

    url_test['url_num_open_parenthesis'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_open_parenthesis(x))

    url_test['url_num_close_parenthesis'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_close_parenthesis(x))

    url_test['url_num_mod_sign'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_mod_sign(x))

    url_test['url_num_ampersand'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_ampersand(x))

    url_test['url_num_at'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_at(x))

    url_test['has_secure_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_secure_in_string(x))

    url_test['has_account_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_account_in_string(x))

    url_test['has_webscr_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_webscr_in_string(x))

    url_test['has_login_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_login_in_string(x))

    url_test['has_ebayisapi_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_ebayisapi_in_string(x))

    url_test['has_signin_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_signin_in_string(x))

    url_test['has_banking_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_banking_in_string(x))

    url_test['has_confirm_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_confirm_in_string(x))

    url_test['has_blog_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_blog_in_string(x))

    url_test['has_logon_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_logon_in_string(x))

    url_test['has_signon_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_signon_in_string(x))

    url_test['has_loginasp_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_loginasp_in_string(x))

    url_test['has_loginphp_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_loginphp_in_string(x))

    url_test['has_loginhtm_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_loginhtm_in_string(x))

    url_test['has_exe_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_exe_in_string(x))

    url_test['has_zip_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_zip_in_string(x))

    url_test['has_rar_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_rar_in_string(x))

    url_test['has_jpg_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_jpg_in_string(x))

    url_test['has_gif_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_gif_in_string(x))

    url_test['has_viewerphp_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_viewerphp_in_string(x))

    url_test['has_linkeq_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_linkeq_in_string(x))

    url_test['has_getImageasp_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_getImageasp_in_string(x))

    url_test['has_plugins_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_plugins_in_string(x))

    url_test['has_paypal_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_paypal_in_string(x))

    url_test['has_order_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_order_in_string(x))

    url_test['has_dbsysphp_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_dbsysphp_in_string(x))

    url_test['has_configbin_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_configbin_in_string(x))

    url_test['has_downloadphp_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_downloadphp_in_string(x))

    url_test['has_js_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_js_in_string(x))

    url_test['has_payment_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_payment_in_string(x))

    url_test['has_files_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_files_in_string(x))

    url_test['has_css_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_css_in_string(x))

    url_test['has_shopping_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_shopping_in_string(x))

    url_test['has_mailphp_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_mailphp_in_string(x))

    url_test['has_jar_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_jar_in_string(x))

    url_test['has_swf_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_swf_in_string(x))

    url_test['has_cgi_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_cgi_in_string(x))

    url_test['has_php_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_php_in_string(x))

    url_test['has_abuse_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_abuse_in_string(x))

    url_test['has_admin_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_admin_in_string(x))

    url_test['has_bin_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_bin_in_string(x))

    url_test['has_personal_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_personal_in_string(x))

    url_test['has_update_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_update_in_string(x))

    url_test['has_verification_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_verification_in_string(x))

    url_test = url_test.drop(columns=['url'])

    return url_test
