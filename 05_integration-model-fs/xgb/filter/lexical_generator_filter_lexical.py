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

    url_test['url_host_length'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_host_length(x))

    url_test['url_is_https'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_is_https(x))

    url_test['url_ip_in_domain'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_ip_in_domain(x))

    url_test['has_php_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_php_in_string(x))

    url_test['url_number_of_parameters'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_number_of_parameters(x))

    url_test['has_exe_in_string'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.has_exe_in_string(x))

    url_test['url_has_port'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_has_port(x))

    url_test['url_is_digits_in_domain'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_is_digits_in_domain(x))

    url_test['url_path_length'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_path_length(x))

    url_test['url_num_question_mark'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_question_mark(x))

    url_test['url_query_length'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_query_length(x))

    url_test['url_string_entropy'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_string_entropy(x))

    url_test['url_num_periods'] = url_test['url'].apply(lambda x: feature_generation_lexical_function.url_num_periods(x))

    url_test['get_tld'] = url_test['url'].apply(lambda x: get_tld(x))

    url_test['url_scheme'] = url_test['url'].apply(lambda x: url_scheme(x))

    url_test = url_test.drop(columns=['url'])

    return url_test
