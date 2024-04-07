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
        html = get(url, timeout=10)
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
            script = str(script)
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
            script = str(script)
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
            script = str(script)
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
            script = str(script)
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
            script = str(script)
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
            script = str(script)
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
            script = str(script)
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
            script = str(script)
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
            script = str(script)
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
    
    if html:
        word_freq = get_word_freq_dict(html)
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
    
    if html:
        word_freq = get_word_freq_dict(html)
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
    
    if html:
        word_freq = get_word_freq_dict(html)
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
    
    if html:
        word_freq = get_word_freq_dict(html)
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
    
    if html:
        word_freq = get_word_freq_dict(html)
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
    
    if html:
        word_freq = get_word_freq_dict(html)
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
    html = '<!DOCTYPE html>\n<html data-adblockkey="MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBALquDFETXRn0Hr05fUP7EJT77xYnPmRbpMy4vk8KYiHnkNpednjOANJcaXDXcKQJN0nXKZJL7TciJD8AoHXK158CAwEAAQ==_Vvof/EtCrzkV5cVyYorrj7xxTYoSu8Phi6aRNPcdBfhEYgBJlWEf6LLcR7qThjdFx1xp5reeEkpPcmGKaosemw==" xmlns="http://www.w3.org/1999/xhtml" lang="en">\n<head>\n    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\n    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/>\n    <title>tobogo.net</title>\n    <style media="screen">\n.asset_star0 {\n\tbackground: url(\'//d38psrni17bvxu.cloudfront.net/themes/assets/star0.gif\') no-repeat center;\n\twidth: 13px;\n\theight: 12px;\n\tdisplay: inline-block;\n}\n\n.asset_star1 {\n\tbackground: url(\'//d38psrni17bvxu.cloudfront.net/themes/assets/star1.gif\') no-repeat center;\n\twidth: 13px;\n\theight: 12px;\n\tdisplay: inline-block;\n}\n\n.asset_starH {\n\tbackground: url(\'//d38psrni17bvxu.cloudfront.net/themes/assets/starH.gif\') no-repeat center;\n\twidth: 13px;\n\theight: 12px;\n\tdisplay: inline-block;\n}\n\n.sitelink {\n\tpadding-right: 16px;\n}\n\n.sellerRatings a:link,\n.sellerRatings a:visited,\n.sellerRatings a:hover,\n.sellerRatings a:active {\n\ttext-decoration: none;\n\tcursor: text;\n}\n\n.sellerRatings {\n\tmargin:0 0 3px 20px;\n}\n\n.sitelinkHolder {\n\tmargin:-15px 0 15px 35px;\n}\n\n#ajaxloaderHolder {\n\tdisplay: block;\n\twidth: 24px;\n\theight: 24px;\n\tbackground: #fff;\n\tpadding: 8px 0 0 8px;\n\tmargin:10px auto;\n\t-webkit-border-radius: 4px;\n\t-moz-border-radius: 4px;\n\tborder-radius: 4px;\n}</style>    <style media="screen">\n* {\n    margin:0;padding:0\n}\n\nbody {\n    background:#101c36;\n    font-family: sans-serif;\n    text-align: center;\n    font-size:1rem;\n}\n\n.header {\n    padding:1rem 1rem 0;\n    overflow:hidden;\n}\n\nh1 {\n    color:#848484;\n    font-size:1.5rem;\n}\n\n.header-text-color:visited,\n.header-text-color:link,\n.header-text-color {\n    color:#848484;\n}\n\n.comp-is-parked {\n  margin: 4px 0 2px;\n}\n\n.comp-sponsored {\n  text-align: left;\n  margin: 0 0 -1.8rem 4px;\n}\n\n.wrapper1 {\n    margin:1rem;\n}\n\n.wrapper2 {\n    background:url(\'//d38psrni17bvxu.cloudfront.net/themes/cleanPeppermintBlack_657d9013/img/bottom.png\') no-repeat center bottom;\n    padding-bottom:140px;\n}\n\n.wrapper3 {\n    background:#fff;\n    max-width:300px;\n    margin:0 auto 1rem;\n    padding-top:1px;\n    padding-bottom:1px;\n}\n\n.onDesktop {\n    display:none;\n}\n\n.tcHolder {\n    padding-top: 2rem;\n}\n\n.adsHolder {\n    margin: 1rem 0;\n    padding-top: 2rem;\n    overflow:hidden;\n}\n\n.footer {\n    color:#626574;\n    padding:2rem 1rem;\n    font-size:.8rem;\n    margin:0 auto;\n    max-width:440px;\n}\n\n.footer a:link,\n.footer a:visited {\n    color:#626574;\n}\n\n.sale_link_bold a,\n.sale_link,\n.sale_link a {\n    color:#626574 !important;\n}\n\n.searchHolder {\n    padding:1px 0 1px 1px;\n    margin:1rem auto;\n    width: 95%;\n    max-width: 500px;\n}\n\n@media screen and (min-width:600px) {\n\n    .comp-is-parked,\n    .comp-sponsored {\n      color: #848484;\n    }\n\n    .comp-sponsored {\n      margin-left: 0;\n    }\n\n    .wrapper1 {\n        max-width:1500px;\n        margin-left:auto;\n        margin-right:auto;\n    }\n\n    .wrapper2 {\n        background:url(\'//d38psrni17bvxu.cloudfront.net/themes/cleanPeppermintBlack_657d9013/img/arrows.png\') no-repeat center top;\n        padding-bottom:0;\n        min-height:600px;\n    }\n\n    .wrapper3 {\n        max-width:530px;\n        background:none;\n    }\n}\n</style>    \n    </head>\n\n<body id="afd" style="visibility:hidden"><div id="plBanner"><script id="parklogic" type="text/javascript" src="http://parking.parklogic.com/page/enhance.js?pcId=12&domain=tobogo.net"></script></div>\n\n<div class="wrapper1">\n        <div class="wrapper2">\n        <div class="wrapper3">\n            <div class="header" id="domainname">\n        <h1>tobogo.net</h1>\n    </div>\n            <div class="tcHolder">\n                <div id="tc"></div>\n            </div>\n        </div>\n    </div>\n            <div class="footer">\n            2024 Copyright.  All Rights Reserved.\n<br/><br/>\n<a href="javascript:void(0);" onClick="window.open(\'/privacy.html\', \'privacy-policy\', \'width=890,height=330,left=200,top=200,menubar=no,status=yes,toolbar=no\').focus()" class="privacy-policy">\n    Privacy Policy\n</a>\n<br/><br/>\n<br/><br/>\n    </div>\n</div>\n\n<script type="text/javascript" language="JavaScript">\n    var tcblock = {\n        // Required and steady\n        \'container\': \'tc\',\n        \'type\': \'relatedsearch\',\n        \'colorBackground\': \'transparent\',\n        \n        \'number\': 3,\n        \n        // Font-Sizes and Line-Heights\n        \'fontSizeAttribution\': 14,\n        \'fontSizeTitle\': 24,\n        \'lineHeightTitle\': 34,\n        // Colors\n        \'colorAttribution\': \'#aaa\',\n        \'colorTitleLink\': \'#0277bd\',\n        // Alphabetically\n        \'horizontalAlignment\': \'center\',\n        \'noTitleUnderline\': false,\n        \'rolloverLinkColor\': \'#01579b\',\n        \'verticalSpacing\': 10\n    };\n    var searchboxBlock = {\n        \'container\': \'search\',\n        \'type\': \'searchbox\',\n        \'fontSizeSearchInput\': 12,\n        \'hideSearchInputBorder\': false,\n        \'hideSearchButtonBorder\': true,\n        \'fontSizeSearchButton\': 13,\n        \'colorBackground\': \'transparent\',\n        \'colorSearchButton\': \'#0b3279\',\n        \'colorSearchButtonText\': \'#fff\'\n    };\n    </script>\n<script type="text/javascript">var isAdult=false;         var containerNames=[];         var uniqueTrackingID=\'MTcxMDEzNTk1NS42MTc0OjU5YjNkYzQ1NWU4Nzk3NjkwM2QxMDNmYTVkYmVlZmJlOTUzYTZhYjY1Y2E0ZDdhYmIwMDkwMDY0YjY3Njk2MmY6NjVlZTlhOTM5NmJjYw==\';         var search=\'\';         var themedata=\'fENsZWFuUGVwcGVybWludEJsYWNrfHw1Y2U4NHxidWNrZXQxMDF8fHx8fHw2NWVlOWE5Mzk2Yjk4fHx8MTcxMDEzNTk1NS42MjgzfDViN2U5ODAwOGE3ZjE1YzdlNTMzOGJhYmVlOTVmNWNjNmEzZmIyYWF8fHx8fDF8fDB8MHx8fHwxfHx8fHwwfDB8fHx8fHx8fHx8MHwwfHwwfHx8MHwwfFcxMD18fDF8VzEwPXxhNzYxMDA3Y2MwNGU2NzY1ZmI3ZjdiMzE2YjljY2Y2OTE5MTM1Yzg4fDB8ZHAtdGVhbWludGVybmV0MDlfM3BofDB8MHx8\';         var domain=\'tobogo.net\';         var scriptPath=\'\';         var adtest=\'off\';if(top.location!==location) { top.location.href=location.protocol + \'//\' + location.host + location.pathname + (location.search ? location.search + \'&\' : \'?\') + \'_xafvr=NDlkN2FlYmIyOWExNjVmOGQ4ZTAyNTFmNTMyYzQ4ZTZkN2YyNWM3Miw2NWVlOWE5Mzk5NjY5\'; }var pageLoadedCallbackTriggered = false;var fallbackTriggered = false;var formerCalledArguments = false;var pageOptions = {\'pubId\': \'dp-teaminternet01\',\'resultsPageBaseUrl\': \'//\' + location.host + \'/?ts=\',\'fontFamily\': \'arial\',\'optimizeTerms\': true,\'maxTermLength\': 40,\'adtest\': true,\'clicktrackUrl\': \'//\' + location.host + \'/track.php?\',\'attributionText\': \'Ads\',\'colorAttribution\': \'#b7b7b7\',\'fontSizeAttribution\': 16,\'attributionBold\': false,\'rolloverLinkBold\': false,\'fontFamilyAttribution\': \'arial\',\'adLoadedCallback\': function(containerName, adsLoaded, isExperimentVariant, callbackOptions) {if (!adsLoaded) {try {var ele = document.getElementById(container).getElementsByTagName(\'iframe\')[0];var vars = JSON.parse(ele.name.substr(ele.id.length + 1));if (typeof vars[ele.id].type == "string" && vars[ele.id].type == "relatedsearch") {relatedFallback((function () {relatedCallback(vars[ele.id]);}));}} catch (err) {if (!(err instanceof SyntaxError)) {throw err;}}} else if (containerName in containerNames) {var data = {containerName: containerName,adsLoaded: adsLoaded,isExperimentVariant: isExperimentVariant,callbackOptions: callbackOptions,terms: pageOptions.terms};ajaxQuery(scriptPath + "/track.php"+ "?toggle=adloaded"+ "&uid=" + encodeURIComponent(uniqueTrackingID)+ "&domain=" + encodeURIComponent(domain)+ "&data=" + encodeURIComponent(JSON.stringify(data)));}},\'pageLoadedCallback\': function (requestAccepted, status) {document.body.style.visibility = \'visible\';pageLoadedCallbackTriggered = true;if ((status.faillisted === true || status.faillisted == "true" || status.blocked === true || status.blocked == "true" ) && status.error_code != 25) {ajaxQuery(scriptPath + "/track.php?domain=" + encodeURIComponent(domain) + "&caf=1&toggle=block&reason=other&uid=" + encodeURIComponent(uniqueTrackingID));}if (status.errorcode && !status.error_code) {status.error_code = status.errorcode;}if (status.error_code) {ajaxQuery(scriptPath + "/track.php?domain=" + encodeURIComponent(domain) + "&caf=1&toggle=errorcode&code=" + encodeURIComponent(status.error_code) + "&uid=" + encodeURIComponent(uniqueTrackingID));if ([18, 19].indexOf(parseInt(status.error_code)) != -1 && fallbackTriggered == false) {fallbackTriggered = true;if (typeof loadFeed === "function") {window.location.href = \'//\' + location.host;}}if (status.error_code == 20) {window.location.replace("//dp.g.doubleclick.net/apps/domainpark/domainpark.cgi?client=" + encodeURIComponent((pageOptions.pubid.match(/^ca-/i) ? "" : "ca-") + pageOptions.pubid) + "&domain_name=" + encodeURIComponent(domain) + "&output=html&drid=" + encodeURIComponent(pageOptions.domainRegistrant));}}if (status.needsreview === true || status.needsreview == "true") {ajaxQuery(scriptPath + "/track.php?domain=" + encodeURIComponent(domain) + "&caf=1&toggle=needsreview&uid=" + encodeURIComponent(uniqueTrackingID));}if ((status.adult === true || status.adult == "true") && !isAdult) {ajaxQuery(scriptPath + "/track.php?domain=" + encodeURIComponent(domain) + "&caf=1&toggle=adult&uid=" + encodeURIComponent(uniqueTrackingID));} else if ((status.adult === false || status.adult == "false") && isAdult) {ajaxQuery(scriptPath + "/track.php?domain=" + encodeURIComponent(domain) + "&caf=1&toggle=nonadult&uid=" + encodeURIComponent(uniqueTrackingID));}if (requestAccepted) {if (status.feed) {ajaxQuery(scriptPath + "/track.php?domain=" + encodeURIComponent(domain) + "&caf=1&toggle=feed&feed=" + encodeURIComponent(status.feed) + "&uid=" + encodeURIComponent(uniqueTrackingID));}if (status.error_code) {ajaxQuery(scriptPath + "/track.php?domain=" + encodeURIComponent(domain) + "&caf=1&toggle=answercheck&answer=error_" + encodeURIComponent(status.error_code) + "&uid=" + encodeURIComponent(uniqueTrackingID));} else {ajaxQuery(scriptPath + "/track.php?domain=" + encodeURIComponent(domain) + "&caf=1&toggle=answercheck&answer=yes&uid=" + encodeURIComponent(uniqueTrackingID));}} else {ajaxQuery(scriptPath + "/track.php?domain=" + encodeURIComponent(domain) + "&caf=1&toggle=answercheck&answer=rejected&uid=" + encodeURIComponent(uniqueTrackingID));}}};var x = function (obj1, obj2) {if (typeof obj1 != "object")obj1 = {};for (var key in obj2)obj1[key] = obj2[key];return obj1;};function getXMLhttp() {var xmlHttp = null;try {xmlHttp = new XMLHttpRequest();} catch (e) {try {xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");} catch (ex) {try {xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");} catch (exc) {}}}return xmlHttp;}function ajaxQuery(url) {if (adtest == \'on\') return false;xmlHttp = getXMLhttp();if (!xmlHttp) return ajaxBackfill(url);xmlHttp.open("GET", url, false);return xmlHttp.send(null);}function ajaxBackfill(url) {if (adtest == \'on\') return false;if (url.indexOf("&toggle=browserjs") > -1) return false;try {var img = document.createElement(\'img\');img.style.visibility = \'hidden\';img.style.width = \'1px\';img.style.height = \'1px\';img.src = url + "&_t=" + new Date().getTime();document.body.appendChild(img);} catch (e) {}}ajaxQuery(scriptPath + "/track.php?domain=" + encodeURIComponent(domain) + "&toggle=browserjs&uid=" + encodeURIComponent(uniqueTrackingID));x(pageOptions, {resultsPageBaseUrl: \'http://ww12.tobogo.net/?ts=fENsZWFuUGVwcGVybWludEJsYWNrfHw1Y2U4NHxidWNrZXQxMDF8fHx8fHw2NWVlOWE5Mzk2Yjk4fHx8MTcxMDEzNTk1NS42Mjg0fDU2NDJkNmNmZDkzOGNlNDliMTNhMDMxM2ZmNTJiMGVlNTAyYTk4Yzh8fHx8fDF8fDB8MHx8fHwxfHx8fHwwfDB8fHx8fHx8fHx8MHwwfHwwfHx8MHwwfFcxMD18fDF8VzEwPXxhNzYxMDA3Y2MwNGU2NzY1ZmI3ZjdiMzE2YjljY2Y2OTE5MTM1Yzg4fDB8ZHAtdGVhbWludGVybmV0MDlfM3BofDB8MHx8\',hl: \'en\',kw: \'\',terms: \'\',uiOptimize: true, channel: \'000001,bucket101\', pubId: \'dp-teaminternet09_3ph\',adtest: \'off\',personalizedAds: false,clicktrackUrl: \'https://trkpc.net/track.\' + \'php?click=caf\' + \'&domain=tobogo.net&uid=MTcxMDEzNTk1NS42MTc0OjU5YjNkYzQ1NWU4Nzk3NjkwM2QxMDNmYTVkYmVlZmJlOTUzYTZhYjY1Y2E0ZDdhYmIwMDkwMDY0YjY3Njk2MmY6NjVlZTlhOTM5NmJjYw%3D%3D&ts=fENsZWFuUGVwcGVybWludEJsYWNrfHw1Y2U4NHxidWNrZXQxMDF8fHx8fHw2NWVlOWE5Mzk2Yjk4fHx8MTcxMDEzNTk1NS42MjgzfDViN2U5ODAwOGE3ZjE1YzdlNTMzOGJhYmVlOTVmNWNjNmEzZmIyYWF8fHx8fDF8fDB8MHx8fHwxfHx8fHwwfDB8fHx8fHx8fHx8MHwwfHwwfHx8MHwwfFcxMD18fDF8VzEwPXxhNzYxMDA3Y2MwNGU2NzY1ZmI3ZjdiMzE2YjljY2Y2OTE5MTM1Yzg4fDB8ZHAtdGVhbWludGVybmV0MDlfM3BofDB8MHx8&adtest=off\' });x(pageOptions, [] );x(pageOptions, { domainRegistrant:\'as-drid-2910317687964208\' } );function loadFeed() {var s = document.createElement(\'script\');s.src = \'//www.google.com/adsense/domains/caf.js?abp=1\';document.body.appendChild(s);var a = Array.prototype.slice.call(arguments);s.onload = function () {var c = google.ads.domains.Caf;switch (a.length) {case 1:return new c(a[0]);case 2:return new c(a[0], a[1]);case 3:return new c(a[0], a[1], a[2]);case 4:return new c(a[0], a[1], a[2], a[3]);case 5:return new c(a[0], a[1], a[2], a[3], a[4]);}return c.apply(null, a);};}function relatedCallback(options) {return false;}function relatedFallback(callback) {return callback();}</script>\n<script type="text/javascript">var ls = function(xhr, path, token) {\n    xhr.onreadystatechange = function () {\n        if (xhr.readyState === XMLHttpRequest.DONE) {\n            if (xhr.status >= 200 && xhr.status <= 400) {\n                if (xhr.responseText.trim() === \'\') {\n                    return;\n                }\n    \n                console.log(JSON.parse(xhr.responseText))\n            } else {\n                console.log(\'There was a problem with the request.\');\n            }\n        }\n    }\n    \n    xhr.open(\'GET\', path + \'/ls.p\' + \'hp?t=65ee9a93&token=\' + encodeURI(token), true);\n    xhr.send();\n};\nls(new XMLHttpRequest(), scriptPath, \'a761007cc04e6765fb7f7b316b9ccf6919135c88\');</script>\n<script type=\'text/javascript\'>x(pageOptions, { "styleId":1167268112});</script>\n<script>\n    function getLoadFeedArguments() {\n        let arguments = [\n            pageOptions\n        ];\n\n        let possibleArguments = [\'adblock\', \'adblock1\', \'adblock2\', \'tcblock\', \'searchboxBlock\', \'rtblock\', \'rsblock\', \'searchblock\'];\n        for (let i = 0; i < possibleArguments.length; i++) {\n            if (typeof this[possibleArguments[i]] !== \'undefined\') {\n                arguments.push(this[possibleArguments[i]]);\n            }\n        }\n\n        return arguments;\n    }\n</script>\n\n<script type="text/javascript">\n    let pageTwo = !!"";\n    let consentGivenBefore = false;\n\n    window.addEventListener(\'ccm19EmbeddingAccepted\', function (e) {\n        if (shouldGiveConsent()) {\n            giveConsent();\n        }\n    });\n\n    window.addEventListener(\'ccm19WidgetLoaded\', function (e) {\n        // hide summoner\n        document.getElementsByClassName(\'ccm-settings-summoner\')[0].style.display = \'none\'\n\n        if (!pageTwo && !window.CCM.fullConsentGiven) {\n            fireConsentCallback(\'loaded\');\n            window.CCM.openWidget()\n        }\n\n        if (pageTwo && !window.CCM.fullConsentGiven) {\n            x(pageOptions, { ivt: false });\n            loadFeed(...getLoadFeedArguments());\n        }\n    });\n\n    window.addEventListener(\'ccm19WidgetClosed\', function (e) {\n        if (window.CCM.fullConsentGiven === false) {\n            fireConsentCallback(\'rejected\');\n            x(pageOptions, { ivt: false });\n            loadFeed(...getLoadFeedArguments());\n            document.getElementsByTagName(\'body\')[0].style.visibility = \'visible\';\n            consentGivenBefore = false;\n        } else if (shouldGiveConsent()) {\n            giveConsent();\n        }\n    });\n\n    function shouldGiveConsent() {\n        return !consentGivenBefore && window.CCM.fullConsentGiven\n    }\n\n    function giveConsent() {\n        x(pageOptions, { ivt: true });\n        loadFeed(...getLoadFeedArguments());\n        if (!pageTwo) {\n            fireConsentCallback(\'accepted\', window.CCM.ucid);\n        }\n        consentGivenBefore = true;\n    }\n\n    function openConsentWidget() {\n        window.CCM.openControlPanel();\n        fireConsentCallback(\'options\');\n    }\n\n    function fireConsentCallback(answer, ucid = \'\') {\n        if (![\'loaded\', \'accepted\', \'rejected\', \'options\'].includes(answer)) {\n            return;\n        }\n\n        if (answer === \'accepted\' && !ucid) {\n            return;\n        }\n\n        let xhr = new XMLHttpRequest();\n        let url = "/track.php?toggle=consent&uid=" + uniqueTrackingID + "&domain=" + domain + "&answer=" + answer + "&token=" + ucid ;\n        xhr.open("GET", url, true);\n        xhr.send();\n    }\n</script>\n\n\n    \n    <script>\n        loadFeed(...getLoadFeedArguments());\n    </script>\n</body>\n</html>\n'

    print(blank_lines_count(html))