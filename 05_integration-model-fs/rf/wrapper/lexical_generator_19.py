import pandas as pd                     # For data transformation
import feature_generation_lexical_function
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

def lexical_generator(url):

    temp = [[url]]
    url_test = pd.DataFrame(temp, columns=['url'])

    url_test['url_domain_entropy'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_domain_entropy(x))

    url_test['url_is_digits_in_domain'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_is_digits_in_domain(x))

    url_test['url_number_of_digits'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_number_of_digits(x))

    url_test['url_is_https'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_is_https(x))

    url_test['url_path_length'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_path_length(x))

    url_test['url_host_length'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_host_length(x))

    url_test['get_tld'] = url_test['url'].apply(lambda x: get_tld(x))

    url_test['url_domain_len'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_domain_len(x))

    url_test['url_num_subdomain'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_subdomain(x))

    url_test['url_num_periods'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_periods(x))

    url_test['url_num_of_hyphens'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_of_hyphens(x))

    url_test['url_num_underscore'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_underscore(x))

    url_test['url_num_equal'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_equal(x))

    url_test['url_num_forward_slash'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_forward_slash(x))

    url_test['has_login_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_login_in_string(x))

    url_test['has_exe_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_exe_in_string(x))

    url_test['has_linkeq_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_linkeq_in_string(x))

    url_test['has_paypal_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_paypal_in_string(x))

    url_test['has_php_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_php_in_string(x))

    url_test = url_test.drop(columns=['url'])

    return url_test
