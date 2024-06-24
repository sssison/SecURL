import pandas as pd
import feature_generation_lexical_function
import feature_generation_content_function_htmlin
import urllib
import time

def url_scheme(url):
    scheme_lookup = pd.read_csv('lookups/scheme_lookup.csv')
    parsed_url = urllib.parse.urlparse(url)
    parsed_url_scheme = parsed_url.scheme
    try:
        return scheme_lookup[parsed_url_scheme].iloc[0]
    except:
        return 0


def get_tld(url):
    tld_lookup = pd.read_csv('lookups/tld_lookup.csv')
    parsed_url = urllib.parse.urlparse(url)
    tld = parsed_url.netloc.split('.')[-1].split(':')[0]
    try:
        return tld_lookup[tld].iloc[0]
    except:
        return 0

def lexical_generator(feature_list, url):
    temp = [[url]]
    url_test = pd.DataFrame(temp, columns=['url'])

    lexical_function_dict = {'url_length': feature_generation_lexical_function.url_length,
                     'url_ip_in_domain': feature_generation_lexical_function.url_ip_in_domain,
                     'url_domain_entropy': feature_generation_lexical_function.url_domain_entropy,
                     'url_is_digits_in_domain': feature_generation_lexical_function.url_is_digits_in_domain,
                     'url_query_length': feature_generation_lexical_function.url_query_length,
                     'url_number_of_parameters': feature_generation_lexical_function.url_number_of_parameters,
                     'url_number_of_digits': feature_generation_lexical_function.url_number_of_digits,
                     'url_string_entropy': feature_generation_lexical_function.url_string_entropy,
                     'url_is_https': feature_generation_lexical_function.url_is_https,
                     'url_path_length': feature_generation_lexical_function.url_path_length,
                     'url_host_length': feature_generation_lexical_function.url_host_length,
                     'url_number_of_subdirectories': feature_generation_lexical_function.url_number_of_subdirectories,
                     'get_tld': get_tld,
                     'url_domain_len': feature_generation_lexical_function.url_domain_len,
                     'url_num_subdomain': feature_generation_lexical_function.url_num_subdomain,
                     'url_has_port': feature_generation_lexical_function.url_has_port,
                     'url_number_of_fragments': feature_generation_lexical_function.url_number_of_fragments,
                     'url_is_encoded': feature_generation_lexical_function.url_is_encoded,
                     'url_number_of_letters': feature_generation_lexical_function.url_number_of_letters,
                     'url_num_periods': feature_generation_lexical_function.url_num_periods,
                     'url_num_of_hyphens': feature_generation_lexical_function.url_num_of_hyphens,
                     'url_num_underscore': feature_generation_lexical_function.url_num_underscore,
                     'url_num_equal': feature_generation_lexical_function.url_num_equal,
                     'url_num_forward_slash': feature_generation_lexical_function.url_num_forward_slash,
                     'url_num_question_mark': feature_generation_lexical_function.url_num_question_mark,
                     'url_num_semicolon': feature_generation_lexical_function.url_num_semicolon,
                     'url_num_open_parenthesis': feature_generation_lexical_function.url_num_open_parenthesis,
                     'url_num_close_parenthesis': feature_generation_lexical_function.url_num_close_parenthesis,
                     'url_num_mod_sign': feature_generation_lexical_function.url_num_mod_sign,
                     'url_num_ampersand': feature_generation_lexical_function.url_num_ampersand,
                     'url_num_at': feature_generation_lexical_function.url_num_at,
                     'has_secure_in_string': feature_generation_lexical_function.has_secure_in_string,
                     'has_account_in_string': feature_generation_lexical_function.has_account_in_string,
                     'has_webscr_in_string': feature_generation_lexical_function.has_webscr_in_string,
                     'has_login_in_string': feature_generation_lexical_function.has_login_in_string,
                     'has_ebayisapi_in_string': feature_generation_lexical_function.has_ebayisapi_in_string,
                     'has_signin_in_string': feature_generation_lexical_function.has_signin_in_string,
                     'has_banking_in_string': feature_generation_lexical_function.has_banking_in_string,
                     'has_confirm_in_string': feature_generation_lexical_function.has_confirm_in_string,
                     'has_blog_in_string': feature_generation_lexical_function.has_blog_in_string,
                     'has_logon_in_string': feature_generation_lexical_function.has_logon_in_string,
                     'has_signon_in_string': feature_generation_lexical_function.has_signon_in_string,
                     'has_loginasp_in_string': feature_generation_lexical_function.has_loginasp_in_string,
                     'has_loginphp_in_string': feature_generation_lexical_function.has_loginphp_in_string,
                     'has_loginhtm_in_string': feature_generation_lexical_function.has_loginhtm_in_string,
                     'has_exe_in_string': feature_generation_lexical_function.has_exe_in_string,
                     'has_zip_in_string': feature_generation_lexical_function.has_zip_in_string,
                     'has_rar_in_string': feature_generation_lexical_function.has_rar_in_string,
                     'has_jpg_in_string': feature_generation_lexical_function.has_jpg_in_string,
                     'has_gif_in_string': feature_generation_lexical_function.has_gif_in_string,
                     'has_viewerphp_in_string': feature_generation_lexical_function.has_viewerphp_in_string,
                     'has_linkeq_in_string': feature_generation_lexical_function.has_linkeq_in_string,
                     'has_getImageasp_in_string': feature_generation_lexical_function.has_getImageasp_in_string,
                     'has_plugins_in_string': feature_generation_lexical_function.has_plugins_in_string,
                     'has_paypal_in_string': feature_generation_lexical_function.has_paypal_in_string,
                     'has_order_in_string': feature_generation_lexical_function.has_order_in_string,
                     'has_dbsysphp_in_string': feature_generation_lexical_function.has_dbsysphp_in_string,
                     'has_configbin_in_string': feature_generation_lexical_function.has_configbin_in_string,
                     'has_downloadphp_in_string': feature_generation_lexical_function.has_downloadphp_in_string,
                     'has_js_in_string': feature_generation_lexical_function.has_js_in_string,
                     'has_payment_in_string': feature_generation_lexical_function.has_payment_in_string,
                     'has_files_in_string': feature_generation_lexical_function.has_files_in_string,
                     'has_css_in_string': feature_generation_lexical_function.has_css_in_string,
                     'has_shopping_in_string': feature_generation_lexical_function.has_shopping_in_string,
                     'has_mailphp_in_string': feature_generation_lexical_function.has_mailphp_in_string,
                     'has_jar_in_string': feature_generation_lexical_function.has_jar_in_string,
                     'has_swf_in_string': feature_generation_lexical_function.has_swf_in_string,
                     'has_cgi_in_string': feature_generation_lexical_function.has_cgi_in_string,
                     'has_php_in_string': feature_generation_lexical_function.has_php_in_string,
                     'has_abuse_in_string': feature_generation_lexical_function.has_abuse_in_string,
                     'has_admin_in_string': feature_generation_lexical_function.has_admin_in_string,
                     'has_bin_in_string': feature_generation_lexical_function.has_bin_in_string,
                     'has_personal_in_string': feature_generation_lexical_function.has_personal_in_string,
                     'has_update_in_string': feature_generation_lexical_function.has_update_in_string,
                     'has_verification_in_string': feature_generation_lexical_function.has_verification_in_string,
                     'url_scheme': url_scheme}
    
    for feature in feature_list:
        try:
            url_test[feature] = url_test['url'].apply(lambda x: lexical_function_dict[feature](x))
        except:
            pass

    url_test = url_test.drop(columns=['url'])

    return url_test

def content_generator(feature_list, url):
    html = feature_generation_content_function_htmlin.get_single_html(url)
    temp = [[url, html]]
    url_test = pd.DataFrame(temp, columns=['url', 'html'])

    lexical_function_dict = {'url_length': feature_generation_lexical_function.url_length,
                            'url_ip_in_domain': feature_generation_lexical_function.url_ip_in_domain,
                            'url_domain_entropy': feature_generation_lexical_function.url_domain_entropy,
                            'url_is_digits_in_domain': feature_generation_lexical_function.url_is_digits_in_domain,
                            'url_query_length': feature_generation_lexical_function.url_query_length,
                            'url_number_of_parameters': feature_generation_lexical_function.url_number_of_parameters,
                            'url_number_of_digits': feature_generation_lexical_function.url_number_of_digits,
                            'url_string_entropy': feature_generation_lexical_function.url_string_entropy,
                            'url_is_https': feature_generation_lexical_function.url_is_https,
                            'url_path_length': feature_generation_lexical_function.url_path_length,
                            'url_host_length': feature_generation_lexical_function.url_host_length,
                            'url_number_of_subdirectories': feature_generation_lexical_function.url_number_of_subdirectories,
                            'get_tld': get_tld,
                            'url_domain_len': feature_generation_lexical_function.url_domain_len,
                            'url_num_subdomain': feature_generation_lexical_function.url_num_subdomain,
                            'url_has_port': feature_generation_lexical_function.url_has_port,
                            'url_number_of_fragments': feature_generation_lexical_function.url_number_of_fragments,
                            'url_is_encoded': feature_generation_lexical_function.url_is_encoded,
                            'url_number_of_letters': feature_generation_lexical_function.url_number_of_letters,
                            'url_num_periods': feature_generation_lexical_function.url_num_periods,
                            'url_num_of_hyphens': feature_generation_lexical_function.url_num_of_hyphens,
                            'url_num_underscore': feature_generation_lexical_function.url_num_underscore,
                            'url_num_equal': feature_generation_lexical_function.url_num_equal,
                            'url_num_forward_slash': feature_generation_lexical_function.url_num_forward_slash,
                            'url_num_question_mark': feature_generation_lexical_function.url_num_question_mark,
                            'url_num_semicolon': feature_generation_lexical_function.url_num_semicolon,
                            'url_num_open_parenthesis': feature_generation_lexical_function.url_num_open_parenthesis,
                            'url_num_close_parenthesis': feature_generation_lexical_function.url_num_close_parenthesis,
                            'url_num_mod_sign': feature_generation_lexical_function.url_num_mod_sign,
                            'url_num_ampersand': feature_generation_lexical_function.url_num_ampersand,
                            'url_num_at': feature_generation_lexical_function.url_num_at,
                            'has_secure_in_string': feature_generation_lexical_function.has_secure_in_string,
                            'has_account_in_string': feature_generation_lexical_function.has_account_in_string,
                            'has_webscr_in_string': feature_generation_lexical_function.has_webscr_in_string,
                            'has_login_in_string': feature_generation_lexical_function.has_login_in_string,
                            'has_ebayisapi_in_string': feature_generation_lexical_function.has_ebayisapi_in_string,
                            'has_signin_in_string': feature_generation_lexical_function.has_signin_in_string,
                            'has_banking_in_string': feature_generation_lexical_function.has_banking_in_string,
                            'has_confirm_in_string': feature_generation_lexical_function.has_confirm_in_string,
                            'has_blog_in_string': feature_generation_lexical_function.has_blog_in_string,
                            'has_logon_in_string': feature_generation_lexical_function.has_logon_in_string,
                            'has_signon_in_string': feature_generation_lexical_function.has_signon_in_string,
                            'has_loginasp_in_string': feature_generation_lexical_function.has_loginasp_in_string,
                            'has_loginphp_in_string': feature_generation_lexical_function.has_loginphp_in_string,
                            'has_loginhtm_in_string': feature_generation_lexical_function.has_loginhtm_in_string,
                            'has_exe_in_string': feature_generation_lexical_function.has_exe_in_string,
                            'has_zip_in_string': feature_generation_lexical_function.has_zip_in_string,
                            'has_rar_in_string': feature_generation_lexical_function.has_rar_in_string,
                            'has_jpg_in_string': feature_generation_lexical_function.has_jpg_in_string,
                            'has_gif_in_string': feature_generation_lexical_function.has_gif_in_string,
                            'has_viewerphp_in_string': feature_generation_lexical_function.has_viewerphp_in_string,
                            'has_linkeq_in_string': feature_generation_lexical_function.has_linkeq_in_string,
                            'has_getImageasp_in_string': feature_generation_lexical_function.has_getImageasp_in_string,
                            'has_plugins_in_string': feature_generation_lexical_function.has_plugins_in_string,
                            'has_paypal_in_string': feature_generation_lexical_function.has_paypal_in_string,
                            'has_order_in_string': feature_generation_lexical_function.has_order_in_string,
                            'has_dbsysphp_in_string': feature_generation_lexical_function.has_dbsysphp_in_string,
                            'has_configbin_in_string': feature_generation_lexical_function.has_configbin_in_string,
                            'has_downloadphp_in_string': feature_generation_lexical_function.has_downloadphp_in_string,
                            'has_js_in_string': feature_generation_lexical_function.has_js_in_string,
                            'has_payment_in_string': feature_generation_lexical_function.has_payment_in_string,
                            'has_files_in_string': feature_generation_lexical_function.has_files_in_string,
                            'has_css_in_string': feature_generation_lexical_function.has_css_in_string,
                            'has_shopping_in_string': feature_generation_lexical_function.has_shopping_in_string,
                            'has_mailphp_in_string': feature_generation_lexical_function.has_mailphp_in_string,
                            'has_jar_in_string': feature_generation_lexical_function.has_jar_in_string,
                            'has_swf_in_string': feature_generation_lexical_function.has_swf_in_string,
                            'has_cgi_in_string': feature_generation_lexical_function.has_cgi_in_string,
                            'has_php_in_string': feature_generation_lexical_function.has_php_in_string,
                            'has_abuse_in_string': feature_generation_lexical_function.has_abuse_in_string,
                            'has_admin_in_string': feature_generation_lexical_function.has_admin_in_string,
                            'has_bin_in_string': feature_generation_lexical_function.has_bin_in_string,
                            'has_personal_in_string': feature_generation_lexical_function.has_personal_in_string,
                            'has_update_in_string': feature_generation_lexical_function.has_update_in_string,
                            'has_verification_in_string': feature_generation_lexical_function.has_verification_in_string,
                            'url_scheme': url_scheme}
    
    content_function_dict = {'blank_lines_count': feature_generation_content_function_htmlin.blank_lines_count,
                            'blank_spaces_count': feature_generation_content_function_htmlin.blank_spaces_count,
                            'word_count': feature_generation_content_function_htmlin.word_count,
                            'average_word_len': feature_generation_content_function_htmlin.average_word_len,
                            'webpage_size': feature_generation_content_function_htmlin.webpage_size,
                            'webpage_entropy': feature_generation_content_function_htmlin.webpage_entropy,
                            'js_count': feature_generation_content_function_htmlin.js_count,
                            'sus_js_count': feature_generation_content_function_htmlin.sus_js_count,
                            'js_eval_count': feature_generation_content_function_htmlin.js_eval_count,
                            'js_escape_count': feature_generation_content_function_htmlin.js_escape_count,
                            'js_unescape_count': feature_generation_content_function_htmlin.js_unescape_count,
                            'js_find_count': feature_generation_content_function_htmlin.js_find_count,
                            'js_exec_count': feature_generation_content_function_htmlin.js_exec_count,
                            'js_search_count': feature_generation_content_function_htmlin.js_search_count,
                            'js_link_count': feature_generation_content_function_htmlin.js_link_count,
                            'js_winopen_count': feature_generation_content_function_htmlin.js_winopen_count,
                            'title_tag_presence': feature_generation_content_function_htmlin.title_tag_presence,
                            'iframe_count': feature_generation_content_function_htmlin.iframe_count,
                            'hyperlink_count': feature_generation_content_function_htmlin.hyperlink_count,
                            'embed_tag_count': feature_generation_content_function_htmlin.embed_tag_count,
                            'object_tag_count': feature_generation_content_function_htmlin.object_tag_count,
                            'meta_tag_count': feature_generation_content_function_htmlin.meta_tag_count,
                            'div_tag_count': feature_generation_content_function_htmlin.div_tag_count,
                            'body_tag_count': feature_generation_content_function_htmlin.body_tag_count,
                            'form_tag_count': feature_generation_content_function_htmlin.form_tag_count,
                            'anchor_tag_count': feature_generation_content_function_htmlin.anchor_tag_count,
                            'applet_tag_count': feature_generation_content_function_htmlin.applet_tag_count,
                            'input_tag_count': feature_generation_content_function_htmlin.input_tag_count,
                            'image_tag_count': feature_generation_content_function_htmlin.image_tag_count,
                            'span_tag_count': feature_generation_content_function_htmlin.span_tag_count,
                            'audio_tag_count': feature_generation_content_function_htmlin.audio_tag_count,
                            'has_log_in_html': feature_generation_content_function_htmlin.has_log_in_html,
                            'has_pay_in_html': feature_generation_content_function_htmlin.has_pay_in_html,
                            'has_free_in_html': feature_generation_content_function_htmlin.has_free_in_html,
                            'has_access_in_html': feature_generation_content_function_htmlin.has_access_in_html,
                            'has_bonus_in_html': feature_generation_content_function_htmlin.has_bonus_in_html,
                            'has_click_in_html': feature_generation_content_function_htmlin.has_click_in_html}
    
    for feature in feature_list:
        try:
            if feature in lexical_function_dict:
                url_test[feature] = url_test['url'].apply(lambda x: lexical_function_dict[feature](x))
            elif feature in content_function_dict:
                url_test[feature] = url_test['url'].apply(lambda x: content_function_dict[feature](x))
        except:
            pass

    url_test = url_test.drop(columns=['url', 'html'])

    return url_test

if __name__ == '__main__':
    url = 'https://www.reddit.com'
    lexical_function_dict = {'url_length': feature_generation_lexical_function.url_length,
                     'url_ip_in_domain': feature_generation_lexical_function.url_ip_in_domain,
                     'url_domain_entropy': feature_generation_lexical_function.url_domain_entropy,
                     'url_is_digits_in_domain': feature_generation_lexical_function.url_is_digits_in_domain,
                     'url_query_length': feature_generation_lexical_function.url_query_length,
                     'url_number_of_parameters': feature_generation_lexical_function.url_number_of_parameters,
                     'url_number_of_digits': feature_generation_lexical_function.url_number_of_digits,
                     'url_string_entropy': feature_generation_lexical_function.url_string_entropy,
                     'url_is_https': feature_generation_lexical_function.url_is_https,
                     'url_path_length': feature_generation_lexical_function.url_path_length,
                     'url_host_length': feature_generation_lexical_function.url_host_length,
                     'url_number_of_subdirectories': feature_generation_lexical_function.url_number_of_subdirectories,
                     'get_tld': get_tld,
                     'url_domain_len': feature_generation_lexical_function.url_domain_len,
                     'url_num_subdomain': feature_generation_lexical_function.url_num_subdomain,
                     'url_has_port': feature_generation_lexical_function.url_has_port,
                     'url_number_of_fragments': feature_generation_lexical_function.url_number_of_fragments,
                     'url_is_encoded': feature_generation_lexical_function.url_is_encoded,
                     'url_number_of_letters': feature_generation_lexical_function.url_number_of_letters,
                     'url_num_periods': feature_generation_lexical_function.url_num_periods,
                     'url_num_of_hyphens': feature_generation_lexical_function.url_num_of_hyphens,
                     'url_num_underscore': feature_generation_lexical_function.url_num_underscore,
                     'url_num_equal': feature_generation_lexical_function.url_num_equal,
                     'url_num_forward_slash': feature_generation_lexical_function.url_num_forward_slash,
                     'url_num_question_mark': feature_generation_lexical_function.url_num_question_mark,
                     'url_num_semicolon': feature_generation_lexical_function.url_num_semicolon,
                     'url_num_open_parenthesis': feature_generation_lexical_function.url_num_open_parenthesis,
                     'url_num_close_parenthesis': feature_generation_lexical_function.url_num_close_parenthesis,
                     'url_num_mod_sign': feature_generation_lexical_function.url_num_mod_sign,
                     'url_num_ampersand': feature_generation_lexical_function.url_num_ampersand,
                     'url_num_at': feature_generation_lexical_function.url_num_at,
                     'has_secure_in_string': feature_generation_lexical_function.has_secure_in_string,
                     'has_account_in_string': feature_generation_lexical_function.has_account_in_string,
                     'has_webscr_in_string': feature_generation_lexical_function.has_webscr_in_string,
                     'has_login_in_string': feature_generation_lexical_function.has_login_in_string,
                     'has_ebayisapi_in_string': feature_generation_lexical_function.has_ebayisapi_in_string,
                     'has_signin_in_string': feature_generation_lexical_function.has_signin_in_string,
                     'has_banking_in_string': feature_generation_lexical_function.has_banking_in_string,
                     'has_confirm_in_string': feature_generation_lexical_function.has_confirm_in_string,
                     'has_blog_in_string': feature_generation_lexical_function.has_blog_in_string,
                     'has_logon_in_string': feature_generation_lexical_function.has_logon_in_string,
                     'has_signon_in_string': feature_generation_lexical_function.has_signon_in_string,
                     'has_loginasp_in_string': feature_generation_lexical_function.has_loginasp_in_string,
                     'has_loginphp_in_string': feature_generation_lexical_function.has_loginphp_in_string,
                     'has_loginhtm_in_string': feature_generation_lexical_function.has_loginhtm_in_string,
                     'has_exe_in_string': feature_generation_lexical_function.has_exe_in_string,
                     'has_zip_in_string': feature_generation_lexical_function.has_zip_in_string,
                     'has_rar_in_string': feature_generation_lexical_function.has_rar_in_string,
                     'has_jpg_in_string': feature_generation_lexical_function.has_jpg_in_string,
                     'has_gif_in_string': feature_generation_lexical_function.has_gif_in_string,
                     'has_viewerphp_in_string': feature_generation_lexical_function.has_viewerphp_in_string,
                     'has_linkeq_in_string': feature_generation_lexical_function.has_linkeq_in_string,
                     'has_getImageasp_in_string': feature_generation_lexical_function.has_getImageasp_in_string,
                     'has_plugins_in_string': feature_generation_lexical_function.has_plugins_in_string,
                     'has_paypal_in_string': feature_generation_lexical_function.has_paypal_in_string,
                     'has_order_in_string': feature_generation_lexical_function.has_order_in_string,
                     'has_dbsysphp_in_string': feature_generation_lexical_function.has_dbsysphp_in_string,
                     'has_configbin_in_string': feature_generation_lexical_function.has_configbin_in_string,
                     'has_downloadphp_in_string': feature_generation_lexical_function.has_downloadphp_in_string,
                     'has_js_in_string': feature_generation_lexical_function.has_js_in_string,
                     'has_payment_in_string': feature_generation_lexical_function.has_payment_in_string,
                     'has_files_in_string': feature_generation_lexical_function.has_files_in_string,
                     'has_css_in_string': feature_generation_lexical_function.has_css_in_string,
                     'has_shopping_in_string': feature_generation_lexical_function.has_shopping_in_string,
                     'has_mailphp_in_string': feature_generation_lexical_function.has_mailphp_in_string,
                     'has_jar_in_string': feature_generation_lexical_function.has_jar_in_string,
                     'has_swf_in_string': feature_generation_lexical_function.has_swf_in_string,
                     'has_cgi_in_string': feature_generation_lexical_function.has_cgi_in_string,
                     'has_php_in_string': feature_generation_lexical_function.has_php_in_string,
                     'has_abuse_in_string': feature_generation_lexical_function.has_abuse_in_string,
                     'has_admin_in_string': feature_generation_lexical_function.has_admin_in_string,
                     'has_bin_in_string': feature_generation_lexical_function.has_bin_in_string,
                     'has_personal_in_string': feature_generation_lexical_function.has_personal_in_string,
                     'has_update_in_string': feature_generation_lexical_function.has_update_in_string,
                     'has_verification_in_string': feature_generation_lexical_function.has_verification_in_string,
                     'url_scheme': url_scheme}
    lexical_feature_list = ['url_host_length',  'url_is_https',  'url_ip_in_domain',  'has_php_in_string',  'url_number_of_parameters',  'has_exe_in_string',  'url_has_port',  'url_is_digits_in_domain',  'url_path_length',  'url_num_question_mark',  'url_query_length',  'url_string_entropy',  'url_num_periods',  'get_tld',  'url_scheme']
    print(len(lexical_feature_list))
    s = time.time()
    lexical_generator(lexical_feature_list, url)
    e = time.time()
    print('Lexical Generation Time: ', e - s)
