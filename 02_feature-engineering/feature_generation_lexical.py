import socket
import urllib
from re import compile
from math import log
from socket import gethostbyname
from requests import get

# TO DO FOR LEXICAL:
# Number of tokens in URL function
# Special char count function (dunno which special characters to include)
# Entropy of URL string function (dunno what this is yet)
# Geolocation of URL host function
# Domain based functions
# Alexa rank of url function

class LexicalFeatures:
    def __init__(self, url):
        self.url = url
        self.parsedurl = urllib.parse.urlparse(self.url)
        self.hostname = self.__get_ip()

    def __get_entropy(self, text):
        text = text.lower()
        probs = [text.count(c) / len(text) for c in set(text)]
        entropy = -sum([p * log(p) / log(2.0) for p in probs])
        return entropy
    
    def __get_ip(self):
        try:
            ip = self.parsedurl.netloc if self.url_host_is_ip() else gethostbyname(self.parsedurl.netloc)
            return ip
        except:
            return None

    #Lexical feature generation functions beyond this point.
    
    def url_scheme(self):   # Requires label encoding
        print(self.url)
        print(self.parsedurl)
        return self.parsedurl.scheme()

    def url_length(self):
        return len(self.url)

    '''
    def url_ip_in_host(self):
        host = self.parsedurl.netloc
        pattern = compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
        match = pattern.match(host)
        if match != None:
            return 1
        else:
            return 0
    ''' # not sure if this pertains to host or domain name so i commented it out for now

    def url_query_length(self):
        return(len(self.parsedurl.query))

    def url_number_of_parameters(self):
        params = self.parsedurl.query
        if params == '':
            return 0
        else:
            return len(params.split('&'))

    def url_number_of_digits(self):
        digit_count = 0
        for i in self.url:
            if i.isdigit():
                digit_count += 1
        return digit_count

    def url_string_entropy(self):
        return self.__get_entropy(self.url)

    def url_is_https(self):
        if self.parsedurl.scheme() == 'https':
            return 1
        else:
            return

    def url_path_length(self):
        return len(self.parsedurl.path)

    '''
    def url_host_length(self):
        return len(self.parsedurl.netloc)
    '''    # not sure if this pertains to host or domain name so i commented it out for now

    def url_number_of_subdirectories(self):
        d = self.parsedurl.path.split('/')
        return len(d)

    def get_tld(self):
      return self.parsedurl.netloc.split('.')[-1].split(':')[0]

    def url_has_port(self):
        split_netloc = self.parsedurl.netloc.split(':')
        if len(split_netloc) > 1 and split_netloc[-1].isdigit():
            return 1

    def url_number_of_fragments(self):
        frags = self.parsedurl.fragment
        if frags == '':
            return len(frags.split('#')) - 1
        else:
            return 0

    def url_is_encoded(self):
        if '%' in self.url.lower():
            return 1
        else:
            return 0

    # Char counts beyond this point

    def url_number_of_letters(self):
        letter_count = 0
        for i in self.url:
            if i.isalpha():
                letter_count += 1
        return letter_count

    def url_num_periods(self):
        period_count = 0
        for i in self.url:
            if i == '.':
                period_count += 1
        return period_count

    def url_num_of_hyphens(self):
        hyphen_count = 0
        for i in self.url:
            if i == '-':
                hyphen_count += 1
        return hyphen_count

    def url_num_underscore(self):
        underscore_count = 0
        for i in self.url:
            if i == '_':
                underscore_count += 1
        return underscore_count
    
    def url_num_equal(self):
        equal_count = 0
        for i in self.url:
            if i == '=':
                equal_count += 1
        return equal_count

    def url_num_forward_slash(self):
        forward_slash_count = 0
        for i in self.url:
            if i == '/':
                forward_slash_count += 1
        return forward_slash_count
    
    def url_num_question_mark(self):
        question_mark_count = 0
        for i in self.url:
            if i == '?':
                question_mark_count += 1
        return question_mark_count

    def url_num_semicolon(self):
        semicolon_count = 0
        for i in self.url:
            if i == ';':
                semicolon_count += 1
        return semicolon_count
    
    def url_num_open_parenthesis(self):
        open_parenthesis_count = 0
        for i in self.url:
            if i == '(':
                open_parenthesis_count += 1
        return open_parenthesis_count
    
    def url_num_close_parenthesis(self):
        close_parenthesis_count = 0
        for i in self.url:
            if i == ')':
                close_parenthesis_count += 1
        return close_parenthesis_count

    def url_num_mod_sign(self):
        mod_sign_count = 0
        for i in self.url:
            if i == '%':
                mod_sign_count += 1
        return mod_sign_count
    
    def url_num_ampersand(self):
        ampersand_count = 0
        for i in self.url:
            if i == '&':
                ampersand_count += 1
        return ampersand_count
    
    def url_num_at(self):
        at_count = 0
        for i in self.url:
            if i == '@':
                at_count += 1
        return at_count

    # Keyword presence beyond this point

    def has_secure_in_string(self):
        if 'secure' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_account_in_string(self):
        if 'account' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_webscr_in_string(self):
        if 'webscr' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_login_in_string(self):
        if 'login' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_ebayisapi_in_string(self):
        if 'ebayisapi' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_signin_in_string(self):
        if 'signin' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_banking_in_string(self):
        if 'banking' in self.url.lower():
            return 1
        else:
            return 0
    
    def has_confirm_in_string(self):
        if 'confirm' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_blog_in_string(self):
        if 'blog' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_logon_in_string(self):
        if 'logon' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_signon_in_string(self):
        if 'signon' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_loginasp_in_string(self):
        if 'login.asp' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_loginphp_in_string(self):
        if 'login.php' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_loginhtm_in_string(self):
        if 'login.htm' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_exe_in_string(self):
        if '.exe' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_zip_in_string(self):
        if '.zip' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_rar_in_string(self):
        if '.rar' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_jpg_in_string(self):
        if '.jpg' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_gif_in_string(self):
        if '.gif' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_viewerphp_in_string(self):
        if 'viewer.php' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_linkeq_in_string(self):
        if 'link=' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_getImageasp_in_string(self):
        if 'getimage.asp' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_plugins_in_string(self):
        if 'plugins' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_paypal_in_string(self):
        if 'paypal' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_order_in_string(self):
        if 'order' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_dbsysphp_in_string(self):
        if 'dbsys.php' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_configbin_in_string(self):
        if 'config.bin' in self.url.lower():
            return 1
        else:
            return 0

    def has_downloadphp_in_string(self):
        if 'download.php' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_js_in_string(self):
        if '.js' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_payment_in_string(self):
        if 'payment' in self.url.lower():
            return 1
        else:
            return 0
    
    def has_files_in_string(self):
        if 'files' in self.url.lower():
            return 1
        else:
            return 0
    
    def has_css_in_string(self):
        if 'css' in self.url.lower():
            return 1
        else:
            return 0

    def has_shopping_in_string(self):
        if 'shopping' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_mailphp_in_string(self):
        if 'mail.php' in self.url.lower():
            return 1
        else:
            return 0

    def has_jar_in_string(self):
        if '.jar' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_swf_in_string(self):
        if '.swf' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_cgi_in_string(self):
        if '.cgi' in self.url.lower():
            return 1
        else:
            return 0

    def has_php_in_string(self):
        if '.php' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_abuse_in_string(self):
        if 'abuse' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_admin_in_string(self):
        if 'admin' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_bin_in_string(self):
        if '.bin' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_personal_in_string(self):
        if 'personal' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_update_in_string(self):
        if 'update' in self.url.lower():
            return 1
        else:
            return 0
        
    def has_verification_in_string(self):
        if 'verification' in self.url.lower():
            return 1
        else:
            return 0

if __name__ == "__main__":
    url = "https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset/data"

    x = LexicalFeatures(url)