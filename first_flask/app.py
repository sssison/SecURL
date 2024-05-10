import flask
from flask import request, jsonify
from random import randint
from first_flask.model_predictor import predict_maliciousness_lexical, predict_maliciousness_content
from time import time
import feature_generator
from whitelist_checker import is_dom_top
from xgboost import Dmatrix

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>SecURL API Framework</h1>
                <p>A flask api implementation for SecURL.   </p>'''

@app.route('/securl', methods=['GET'])
def check_url():
    """
    Analyzes the URL and checks whether it is malicious or not, based on the result of the trained classifiers
    Steps:
        1. Checking something (bencio-specific)
        2. is_top_domain(): input - string url; output - int
        3. feature_generator(): input - string list feature_list, string url; output - pd.df url_features
        4. predict_maliciousness(): input - DMatrix url_features, boolean is_secure; output - int 
        5. database_insert(): input - tuple (string url, string date, int prediction, int actual); output - NA
        6. return
    """

    inp_url = "(example url)"
    is_secure = False 
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
    
    # Input validation: checks if URL is in request
    if 'inp_url' in request.args:
        inp_url = request.args['inp_url']
    
    # Input validation: checks if is_secure is in request
    if 'is_secure' in request.args:
        is_secure = (request.args['is_secure']=='enabled')

    # ! temporary: strip off prefixes
    inp_url = inp_url.replace("https://","",1)
    inp_url = inp_url.replace("http://","",1)

    # check time and select the algorithm
    # TODO: replace the algorithms below with lexical-based and content-based detection
    # TEMPORARY: XGB for basic security (is_secure==False), RF for enhanced security (is_secure==True) 
    time_start = time()
    in_td = is_dom_top(inp_url)

    if in_td==1:
        prediction = "Benign"
    else:
        # Generate URL Features
        if (is_secure == 0):
            url_features_pandas = feature_generator.lexical_generator(temp_list_lexical, inp_url)

            # Convert pd.df to Dmatrix
            url_features = Dmatrix(url_features_pandas)

            # Generate prediction
            prediction = predict_maliciousness_lexical(url_features)

        else:
            try:
                url_features_pandas = feature_generator.content_generator(temp_list_content, inp_url)

                # Convert pd.df to Dmatrix
                url_features = Dmatrix(url_features_pandas)

                # Generate prediction
                prediction = predict_maliciousness_content(url_features)
                isFetchable = 1
            except:
                isFetchable = 0

    time_end = time()
    random_score = randint(0,100)

    return dict(
        status=200,
        score=random_score,
        safety=(random_score>60),
        url=inp_url,
        time=(time_end-time_start),
        message=prediction
    )
    """
    Future reference:
    - for obtaining domain only:
        from urllib.parse import urlparse
        domain = urlparse('http://www.example.test.co.uk/foo/bar').netloc
        print(domain) //// outputs www.example.test.co.uk
    """

@app.route('/securl/feedback', methods=['GET'])
def report_url():
    """
    Receives reports on incorrect detection and saves to SQLite database
    """
    inp_url = "(example url)"
    is_secure = False
    
    if 'url' in request.args:
        inp_url = request.args['url']
    
    if 'correct' in request.args:
        print("Report received!\n")
        print(f"URL {inp_url} should have been {request.args['correct']} instead of {request.args['predicted']} ")

    return dict(
        status=200
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)