import socket
import urllib
from re import compile
from math import log
from socket import gethostbyname
from requests import get
import tldextract

def get_entropy(text):
    text = text.lower()
    probs = [text.count(c) / len(text) for c in set(text)]
    entropy = -sum([p * log(p) / log(2.0) for p in probs])
    return entropy

def get_ip(url):
    parsed_url = urllib.parse.urlparse(url)
    try:
        ip = parsed_url.netloc if url_ip_in_domain() else gethostbyname(parsed_url.netloc)
        return ip
    except:
        return None

#Lexical feature generation functions beyond this point.

def url_scheme(url):   # Requires label encoding
    parsed_url = urllib.parse.urlparse(url)
    print(url)
    print(parsed_url)
    return parsed_url.scheme

def url_length(url):
    return len(url)
  
def url_ip_in_domain(url):
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    pattern = compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    match = pattern.match(domain)
    if match != None:
        return 1
    else:
        return 0

def url_domain_entropy(url):
    ext = tldextract.extract(url)
    domain = ext.domain
    return get_entropy(domain)

def url_is_digits_in_domain(url):
    ext = tldextract.extract(url)
    domain = ext.domain
    for i in domain:
        if i.isdigit():
            return 1
    return 0

def url_query_length(url):
    parsed_url = urllib.parse.urlparse(url)
    return(len(parsed_url.query))

def url_number_of_parameters(url):
    parsed_url = urllib.parse.urlparse(url)
    params = parsed_url.query
    if params == '':
        return 0
    else:
        return len(params.split('&'))

def url_number_of_digits(url):
    digit_count = 0
    for i in url:
        if i.isdigit():
            digit_count += 1
    return digit_count

def url_string_entropy(url):
    return get_entropy(url)

def url_is_https(url):
    parsed_url = urllib.parse.urlparse(url)
    if parsed_url.scheme == 'https':
        return 1
    else:
        return 0

def url_path_length(url):
    parsed_url = urllib.parse.urlparse(url)
    return len(parsed_url.path)

def url_host_length(url):
    parsed_url = urllib.parse.urlparse(url)
    return len(parsed_url.netloc)

def url_number_of_subdirectories(url):
    parsed_url = urllib.parse.urlparse(url)
    d = parsed_url.path.split('/')
    return len(d)

def get_tld(url):
  parsed_url = urllib.parse.urlparse(url)
  return parsed_url.netloc.split('.')[-1].split(':')[0]

def url_domain_len(url):
    ext = tldextract.extract(url)
    domain = ext.domain
    return len(domain)

def url_num_subdomain(url):
    return len(url.ext.subdomain.split('.'))

def url_has_port(url):
    parsed_url = urllib.parse.urlparse(url)
    split_netloc = parsed_url.netloc.split(':')
    if len(split_netloc) > 1 and split_netloc[-1].isdigit():
        return 1
    else:
        return 0

def url_number_of_fragments(url):
    parsed_url = urllib.parse.urlparse(url)
    frags = parsed_url.fragment
    if frags == '':
        return len(frags.split('#')) - 1
    else:
        return 0

def url_is_encoded(url):
    if '%' in url.lower():
        return 1
    else:
        return 0

# Char counts beyond this point

def url_number_of_letters(url):
    letter_count = 0
    for i in url:
        if i.isalpha():
            letter_count += 1
    return letter_count

def url_num_periods(url):
    period_count = 0
    for i in url:
        if i == '.':
            period_count += 1
    return period_count

def url_num_of_hyphens(url):
    hyphen_count = 0
    for i in url:
        if i == '-':
            hyphen_count += 1
    return hyphen_count

def url_num_underscore(url):
    underscore_count = 0
    for i in url:
        if i == '_':
            underscore_count += 1
    return underscore_count

def url_num_equal(url):
    equal_count = 0
    for i in url:
        if i == '=':
            equal_count += 1
    return equal_count

def url_num_forward_slash(url):
    forward_slash_count = 0
    for i in url:
        if i == '/':
            forward_slash_count += 1
    return forward_slash_count

def url_num_question_mark(url):
    question_mark_count = 0
    for i in url:
        if i == '?':
            question_mark_count += 1
    return question_mark_count

def url_num_semicolon(url):
    semicolon_count = 0
    for i in url:
        if i == ';':
            semicolon_count += 1
    return semicolon_count

def url_num_open_parenthesis(url):
    open_parenthesis_count = 0
    for i in url:
        if i == '(':
            open_parenthesis_count += 1
    return open_parenthesis_count

def url_num_close_parenthesis(url):
    close_parenthesis_count = 0
    for i in url:
        if i == ')':
            close_parenthesis_count += 1
    return close_parenthesis_count

def url_num_mod_sign(url):
    mod_sign_count = 0
    for i in url:
        if i == '%':
            mod_sign_count += 1
    return mod_sign_count

def url_num_ampersand(url):
    ampersand_count = 0
    for i in url:
        if i == '&':
            ampersand_count += 1
    return ampersand_count

def url_num_at(url):
    at_count = 0
    for i in url:
        if i == '@':
            at_count += 1
    return at_count

# Keyword presence beyond this point

def has_secure_in_string(url):
    if 'secure' in url.lower():
        return 1
    else:
        return 0
    
def has_account_in_string(url):
    if 'account' in url.lower():
        return 1
    else:
        return 0
    
def has_webscr_in_string(url):
    if 'webscr' in url.lower():
        return 1
    else:
        return 0
    
def has_login_in_string(url):
    if 'login' in url.lower():
        return 1
    else:
        return 0
    
def has_ebayisapi_in_string(url):
    if 'ebayisapi' in url.lower():
        return 1
    else:
        return 0
    
def has_signin_in_string(url):
    if 'signin' in url.lower():
        return 1
    else:
        return 0
    
def has_banking_in_string(url):
    if 'banking' in url.lower():
        return 1
    else:
        return 0

def has_confirm_in_string(url):
    if 'confirm' in url.lower():
        return 1
    else:
        return 0
    
def has_blog_in_string(url):
    if 'blog' in url.lower():
        return 1
    else:
        return 0
    
def has_logon_in_string(url):
    if 'logon' in url.lower():
        return 1
    else:
        return 0
    
def has_signon_in_string(url):
    if 'signon' in url.lower():
        return 1
    else:
        return 0
    
def has_loginasp_in_string(url):
    if 'login.asp' in url.lower():
        return 1
    else:
        return 0
    
def has_loginphp_in_string(url):
    if 'login.php' in url.lower():
        return 1
    else:
        return 0
    
def has_loginhtm_in_string(url):
    if 'login.htm' in url.lower():
        return 1
    else:
        return 0
    
def has_exe_in_string(url):
    if '.exe' in url.lower():
        return 1
    else:
        return 0
    
def has_zip_in_string(url):
    if '.zip' in url.lower():
        return 1
    else:
        return 0
    
def has_rar_in_string(url):
    if '.rar' in url.lower():
        return 1
    else:
        return 0
    
def has_jpg_in_string(url):
    if '.jpg' in url.lower():
        return 1
    else:
        return 0
    
def has_gif_in_string(url):
    if '.gif' in url.lower():
        return 1
    else:
        return 0
    
def has_viewerphp_in_string(url):
    if 'viewer.php' in url.lower():
        return 1
    else:
        return 0
    
def has_linkeq_in_string(url):
    if 'link=' in url.lower():
        return 1
    else:
        return 0
    
def has_getImageasp_in_string(url):
    if 'getimage.asp' in url.lower():
        return 1
    else:
        return 0
    
def has_plugins_in_string(url):
    if 'plugins' in url.lower():
        return 1
    else:
        return 0
    
def has_paypal_in_string(url):
    if 'paypal' in url.lower():
        return 1
    else:
        return 0
    
def has_order_in_string(url):
    if 'order' in url.lower():
        return 1
    else:
        return 0
    
def has_dbsysphp_in_string(url):
    if 'dbsys.php' in url.lower():
        return 1
    else:
        return 0
    
def has_configbin_in_string(url):
    if 'config.bin' in url.lower():
        return 1
    else:
        return 0

def has_downloadphp_in_string(url):
    if 'download.php' in url.lower():
        return 1
    else:
        return 0
    
def has_js_in_string(url):
    if '.js' in url.lower():
        return 1
    else:
        return 0
    
def has_payment_in_string(url):
    if 'payment' in url.lower():
        return 1
    else:
        return 0

def has_files_in_string(url):
    if 'files' in url.lower():
        return 1
    else:
        return 0

def has_css_in_string(url):
    if 'css' in url.lower():
        return 1
    else:
        return 0

def has_shopping_in_string(url):
    if 'shopping' in url.lower():
        return 1
    else:
        return 0
    
def has_mailphp_in_string(url):
    if 'mail.php' in url.lower():
        return 1
    else:
        return 0

def has_jar_in_string(url):
    if '.jar' in url.lower():
        return 1
    else:
        return 0
    
def has_swf_in_string(url):
    if '.swf' in url.lower():
        return 1
    else:
        return 0
    
def has_cgi_in_string(url):
    if '.cgi' in url.lower():
        return 1
    else:
        return 0

def has_php_in_string(url):
    if '.php' in url.lower():
        return 1
    else:
        return 0
    
def has_abuse_in_string(url):
    if 'abuse' in url.lower():
        return 1
    else:
        return 0
    
def has_admin_in_string(url):
    if 'admin' in url.lower():
        return 1
    else:
        return 0
    
def has_bin_in_string(url):
    if '.bin' in url.lower():
        return 1
    else:
        return 0
    
def has_personal_in_string(url):
    if 'personal' in url.lower():
        return 1
    else:
        return 0
    
def has_update_in_string(url):
    if 'update' in url.lower():
        return 1
    else:
        return 0
    
def has_verification_in_string(url):
    if 'verification' in url.lower():
        return 1
    else:
        return 0

if __name__ == "__main__":
    url = "qux.bar.foo.example.com"

    print(url_number_of_subdirectories(url))
