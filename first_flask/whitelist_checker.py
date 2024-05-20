import requests
import json
import pandas as pd
from tldextract import extract
import urllib
import time

def is_dom_top(in_url):
    ext = extract(in_url)
    in_domain = ext.registered_domain

    top_domains = pd.read_csv('top10milliondomains.csv', nrows = 1000)
    top_domains = pd.Series(top_domains['Domain'])
    top_domains = top_domains.to_list()
    top_domains.append("upd.edu.ph")

    if in_domain in top_domains:
        return 1
    else:
        return 0

if __name__ == '__main__':
    url = 'https://www.google.com'
    
    s = time.time()
    print(is_dom_top(url))
    e = time.time()
    print('Elapsed time: ', e - s)