import socket
import urllib.parse

# TO DO FOR LEXICAL:
# Number of tokens in URL function
# Special char count function (dunno which special characters to include)
# Entropy of URL string function (dunno what this is yet)
# Geolocation of URL host function
# Domain based functions
# Alexa rank of url function

def get_letter_count(url):
    """
    Takes an input string url and returns the number of letters (in int) present in the url.
    """
    count = 0
    for i in url:
        if i.isalpha():
            count += 1
    return(count)

def get_digit_count(url):
    """
    Takes an input string url and returns the number of single digit integers (in int) present in the url.
    """
    count = 0
    for i in url:
        if i.isdigit():
            count += 1
    return(count)

def get_url_len(url):
    """
    Takes an input string url and returns its length.
    """
    return(len(url))

def get_char_count(url, char):
    """
    Takes an input string url and string char and returns the number of times (in int) the input char is seen in the url.
    """
    count = 0
    for i in url:
        if i == char:
            count += 1
    return(count)

def get_word_presence(url, word):
    """
    Takes an input string url and string word and returns an int 1 if the word is present in the url and an int 0 otherwise.
    """
    if word in url:
        return 1
    else:
        return 0

def parse_url(url):
    """
    Takes and input string url and returns an object that has the deconstructed elements of the url.
    """
    return(urllib.parse.urlparse(url))

def get_ip(parsed_url):
    """
    Takes an input parsed_url object (using urllib.parse.urlparse(url)) and returns its IP address in string.
    """
    return(socket.gethostbyname(parsed_url.netloc))

def get_query_len(parsed_url):
    """
    Takes an input parsed_url object (using urllib.parse.urlparse(url)) and returns its Query string length in int.
    """
    return(len(parsed_url.query))

def get_tld(parsed_url):
    """
    Takes an input parsed_url object (using urllib.parse.urlparse(url)) and returns its top level domain as a string.
    """
    return(parsed_url.netloc)

if __name__ == "__main__":
    url = "https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset/data"

    parsed_url = parse_url(url)
    print(parsed_url)

    print(get_letter_count(url))
    print(get_digit_count(url))
    print(get_ip(parsed_url))
    print(get_query_len(parsed_url))
    print(get_tld(parsed_url))