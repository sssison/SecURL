from urllib.parse import urlparse
from pyquery import PyQuery
from requests import get
from socket import gethostbyname
from numpy import array, log
from string import punctuation
from json import dump, loads
from re import compile
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation

def get_entropy(text):
    text = text.lower()
    probs = [text.count(c) / len(text) for c in set(text)]
    entropy = -sum([p * log(p) / log(2.0) for p in probs])
    return entropy

def get_html(url):
    try:
        if 'http' not in url:
            url = 'http://' + url
        html = get(url, timeout=1)
        html = html.text if html else None
    except:
        html = None
    return html

def get_word_freq_dict(html):
    #taken from: https://stackoverflow.com/questions/46271528/counting-words-inside-a-webpage
    soup = BeautifulSoup(html, features = 'html.parser')
    # We get the words within paragrphs
    text_p = (''.join(s.findAll(string=True))for s in soup.findAll('p'))
    c_p = Counter((x.rstrip(punctuation).lower() for y in text_p for x in y.split()))
    # We get the words within divs
    text_div = (''.join(s.findAll(string=True))for s in soup.findAll('div'))
    c_div = Counter((x.rstrip(punctuation).lower() for y in text_div for x in y.split()))

    return(c_p + c_div)

#Content-based feature generation functions beyond this point.

def blank_lines_count(html):
    blank_lines = 0
    if html:
        for i in html:
            if i == '\n' or i == '\r\n' or i == '\r':
                blank_lines += 1
        return blank_lines
    else:
        return None

def blank_spaces_count(html):
    spaces = 0
    if html:
        for i in html:
            if i == ' ':
                spaces += 1
        return spaces
    else:
        return None

def word_count(html):
    if html:
        word_freq = get_word_freq_dict(html)
        total = 0
        if word_freq:
            for i in word_freq:
                total += word_freq[i]
        return total
    else:
        return None

def average_word_len(html):
    
    if html:
        word_freq = get_word_freq_dict(html)
        total_len = 0
        n_words = 0
        ave_word_len = 0
        if word_freq:
            for i in word_freq:
                total_len += len(i)*word_freq[i]
                n_words += word_freq[i]
                total_len += len(i)*word_freq[i]
                n_words += word_freq[i]

            ave_word_len = total_len/n_words
            return ave_word_len
        else:
            return 0
    else:
        return None

def webpage_size(html):
    
    if html:
        return len(html)
    else:
        return None

def webpage_entropy(html):
    
    if html:
        return(get_entropy(html))
    else:
        return None

#JS count beyond this point

def js_count(html):
    
    if html:
        soup = BeautifulSoup(html, features = 'html.parser')
        return len(soup.find_all('script'))
    else:
        return None
    
def sus_js_count(html):
    
    if html:
        soup = BeautifulSoup(html, features = 'html.parser')
        total = 0
        scripts = soup.find_all('script')
        sus = ['eval', 'escape', 'unescape', 'find', 'exec', 'search', 'link', 'Windows.open']
        for script in scripts:
            for sus_func in sus:
                if sus_func in script:
                    total += 1
        return total
    else:
        return None

def js_eval_count(html):
    
    if html:
        soup = BeautifulSoup(html, features = 'html.parser')
        total = 0
        scripts = soup.find_all('script')
        for script in scripts:
            if 'eval' in script:
                total += 1
        return total
    else:
        return None
    
def js_escape_count(html):
    
    if html:
        soup = BeautifulSoup(html, features = 'html.parser')
        total = 0
        scripts = soup.find_all('script')
        for script in scripts:
            if 'escape' in script:
                total += 1
        return total
    else:
        return None
    
def js_unescape_count(html):
    
    if html:
        soup = BeautifulSoup(html, features = 'html.parser')
        total = 0
        scripts = soup.find_all('script')
        for script in scripts:
            if 'unescape' in script:
                total += 1
        return total
    else:
        return None
    
def js_find_count(html):
    
    if html:
        soup = BeautifulSoup(html, features = 'html.parser')
        total = 0
        scripts = soup.find_all('script')
        for script in scripts:
            if 'find' in script:
                total += 1
        return total
    else:
        return None

def js_exec_count(html):
    
    if html:
        soup = BeautifulSoup(html, features = 'html.parser')
        total = 0
        scripts = soup.find_all('script')
        for script in scripts:
            if 'exec' in script:
                total += 1
        return total
    else:
        return None
    
def js_search_count(html):
    
    if html:
        soup = BeautifulSoup(html, features = 'html.parser')
        total = 0
        scripts = soup.find_all('script')
        for script in scripts:
            if 'search' in script:
                total += 1
        return total
    else:
        return None
    
def js_link_count(html):
    
    if html:
        soup = BeautifulSoup(html, features = 'html.parser')
        total = 0
        scripts = soup.find_all('script')
        for script in scripts:
            if 'link' in script:
                total += 1
        return total
    else:
        return None

def js_winopen_count(html):
    
    if html:
        soup = BeautifulSoup(html, features = 'html.parser')
        total = 0
        scripts = soup.find_all('script')
        for script in scripts:
            if 'Windows.open' in script:
                total += 1
        return total
    else:
        return None

#Tag count/presence beyond this point
#Implementation is inspired from https://copyprogramming.com/howto/is-there-a-way-in-beautiful-soup-to-count-the-number-of-tags-in-a-html-page

def title_tag_presence(html):
    
    if html:
        soup = BeautifulSoup(html, features = 'html.parser')
        if soup.find('title'):
            return 1
        else:
            return 0
    else:
        return None

def iframe_count(html):
    
    if html:
        soup = BeautifulSoup(html, features = 'html.parser')
        return(len(soup.find_all('iframe')))
    else:
        return None
    
def hyperlink_count(html):
    
    if html:
        soup = BeautifulSoup(html, features = 'html.parser')
        return len(soup.find_all('a'))
    else:
        return None

def embed_tag_count(html):
    
    if html:
        soup = BeautifulSoup(html, features = 'html.parser')
        return len(soup.find_all('embed'))
    else:
        return None

def object_tag_count(html):
    
    if html:
        soup = BeautifulSoup(html, features = 'html.parser')
        return len(soup.find_all('object'))
    else:
        return None
    
def meta_tag_count(html):
    
    if html:
        soup = BeautifulSoup(html, features = 'html.parser')
        return len(soup.find_all('meta'))
    else:
        return None
    
def div_tag_count(html):
    
    if html:
        soup = BeautifulSoup(html, features = 'html.parser')
        return len(soup.find_all('div'))
    else:
        return None
    
def body_tag_count(html):
    
    if html:
        soup = BeautifulSoup(html, features = 'html.parser')
        return len(soup.find_all('body'))
    else:
        return None

def form_tag_count(html):
    
    if html:
        soup = BeautifulSoup(html, features = 'html.parser')
        return len(soup.find_all('form'))
    else:
        return None
    
def anchor_tag_count(html):
    
    if html:
        soup = BeautifulSoup(html, features = 'html.parser')
        return len(soup.find_all('anchor'))
    else:
        return None

def applet_tag_count(html):
    
    if html:
        soup = BeautifulSoup(html, features = 'html.parser')
        return len(soup.find_all('applet'))
    else:
        return None

def input_tag_count(html):
    
    if html:
        soup = BeautifulSoup(html, features = 'html.parser')
        return len(soup.find_all('input'))
    else:
        return None
    
def image_tag_count(html):
    
    if html:
        soup = BeautifulSoup(html, features = 'html.parser')
        return len(soup.find_all('image'))
    else:
        return None

def span_tag_count(html):
    
    if html:
        soup = BeautifulSoup(html, features = 'html.parser')
        return len(soup.find_all('span'))
    else:
        return None

def audio_tag_count(html):
    
    if html:
        soup = BeautifulSoup(html, features = 'html.parser')
        return len(soup.find_all('audio'))
    else:
        return None

#Keyword presence beyond this point 
def has_log_in_html(html):
    
    word_freq = get_word_freq_dict(html)
    if html:
        if word_freq:
            if 'log' in word_freq:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return None
    
def has_pay_in_html(html):
    
    word_freq = get_word_freq_dict(html)
    if html:
        if word_freq:
            if 'pay' in word_freq:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return None
    
def has_free_in_html(html):
    
    word_freq = get_word_freq_dict(html)
    if html:
        if word_freq:
            if 'free' in word_freq:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return None
    
def has_access_in_html(html):
    
    word_freq = get_word_freq_dict(html)
    if html:
        if word_freq:
            if 'access' in word_freq:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return None

def has_bonus_in_html(html):
    
    word_freq = get_word_freq_dict(html)
    if html:
        if word_freq:
            if 'bonus' in word_freq:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return None
    
    
def has_click_in_html(html):
    
    word_freq = get_word_freq_dict(html)
    if html:
        if word_freq:
            if 'click' in word_freq:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return None

if __name__ == '__main__':
    url = 'bopsecrets.org/rexroth/cr/1.htm'

    print(blank_spaces_count(url))