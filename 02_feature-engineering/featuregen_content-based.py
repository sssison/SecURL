import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from urllib.parse import urlparse
from pyquery import PyQuery
from requests import get
from socket import gethostbyname
from numpy import array, log
from string import punctuation
from json import dump, loads
from re import compile

class ContentFeatures:
    def __init__(self, url):
        self.url = url
        self.urlparse = urlparse(self.url)
        self.html = self.__get_html()
        self.pq = self.__get_pq()
        self.scripts = self.__get_scripts()
        self.host = self.__get_ip()

    def __get_ip(self):
        try:
            ip = self.urlparse.netloc if self.url_host_is_ip() else gethostbyname(self.urlparse.netloc)
            return ip
        except:
            return None

    def url_host_is_ip(self):
        host = self.urlparse.netloc
        pattern = compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
        match = pattern.match(host)
        return match is not None

    def __get_html(self):
        try:
            html = get(self.url, timeout=5)
            html = html.text if html else None
        except:
            html = None
        return html

    def __get_pq(self):
        try:
            pq = PyQuery(self.html) if self.html else None
            return pq
        except:
            return None


    def __get_scripts(self):
        scripts = self.pq('script') if self.pq else None
        return scripts

    def __get_entropy(self, text):
        text = text.lower()
        probs = [text.count(c) / len(text) for c in set(text)]
        return -sum([p * log(p) / log(2.0) for p in probs])

    # extract content-based features

    def number_of_whitespace(self):
        whitespaces = [i for i in self.html if i == ' ']
        return len(whitespaces)
    
    def number_of_words(self):
        return 1
    
    def number_iframes(self):
        iframes = self.pq('iframe') + self.pq('frame')
        return len(iframes)
    
    def number_of_script_tags(self):
        return len(self.scripts) if self.scripts else None
    
    def number_embeds(self):
        objects = self.pq('embed')
        return len(objects)
    
    def number_objects(self):
        objects = self.pq('object')
        return len(objects)
    
    def number_meta(self):
        meta = self.pq('meta')
        return len(meta)
    
    def number_div(self):
        div = self.pq('div')
        return len(div)
    
    def number_body(self):
        body = self.pq('body')
        return len(body)
    
    def number_form(self):
        form = self.pq('form')
        return len(form)

    def number_title(self):
        title = self.pq('title')
        return len(title)
    
    def number_anchor(self):
        anchor = self.pq('anchor')
        return len(anchor)
    
    def number_applet(self):
        return len(self.pq('applet'))
    
    def number_input(self):
        return len(self.pq('input'))
    
    def number_image(self):
        return len(self.pq('image'))

    def number_span(self):
        return len(self.pq('span'))
    
    # Not sure with style pa
    def number_style(self):
        return len(self.pq('style'))
    
    def number_audio(self):
        return len(self.pq('audio'))
    
    def url_page_entropy(self):
        return self.__get_entropy(self.html)
    
    def number_of_eval_functions(self):
        scripts = self.pq('script')
        scripts = ['eval' in script.text().lower() for script in scripts.items()]
        return sum(scripts)
    
    def number_of_escape_functions(self):
        scripts = self.pq('script')
        scripts = ['escape' in script.text().lower() for script in scripts.items()]
        return sum(scripts)

    def number_of_unescape_functions(self):
        scripts = self.pq('script')
        scripts = ['unescape' in script.text().lower() for script in scripts.items()]
        return sum(scripts)
    
    def number_of_find_functions(self):
        scripts = self.pq('script')
        scripts = ['find' in script.text().lower() for script in scripts.items()]
        return sum(scripts)
    
    def number_of_exec_functions(self):
        scripts = self.pq('script')
        scripts = ['exec' in script.text().lower() for script in scripts.items()]
        return sum(scripts)
    
    def number_of_search_functions(self):
        scripts = self.pq('script')
        scripts = ['search' in script.text().lower() for script in scripts.items()]
        return sum(scripts)

    def number_of_link_functions(self):
        scripts = self.pq('script')
        scripts = ['link' in script.text().lower() for script in scripts.items()]
        return sum(scripts)

url = ContentFeatures("https://facebook.com")

print(url.number_of_link_functions())