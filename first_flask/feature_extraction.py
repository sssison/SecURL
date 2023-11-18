import socket
import urllib.parse

def get_char_count(url, char):
    """
    Takes an input string url and string char and returns the number of times the input char is seen in the url.
    """
    count = 0
    for i in url:
        if i == char:
            count += 1
    return(count)

def get_word_presence(url, word):
    """
    Takes an input string url and string word and returns a 1 if the word is present in the url and 0 otherwise.
    """
    if word in url:
        return 1
    else:
        return 0
    
def get_ip_presence(url):
    """
    Takes an input string url and returns its IP address.
    """
    parsed_url = urllib.parse.urlparse(url)
    return(socket.gethostbyname(parsed_url.netloc))

if __name__ == "__main__":
    print(get_ip_presence("https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset/data"))
