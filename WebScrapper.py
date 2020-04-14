from requests import get;
from requests.exceptions import RequestException;
from contextlib import closing;
from bs4 import BeautifulSoup;

from selenium import webdriver

#from urllib.request import urlopen as uReq;

# temporary, as this value will be read from a txt file

# Probably cannot use stocktwits for now due to all the data I am interested
# in is returned by ajax requests
URL = "https://stocktwits.com/discover/earnings-calendar/";
#URL = "https://stocktwits.com/discover/earnings-calendar/2020-04-14";
#URL = "https://ql.stocktwits.com/batch?symbols=TSRI%2CARTW%2CLONE%2CXELB%2CLOAN%2CPNM%2CHIFS";

def getURL(url):
    try:
        with closing(get(url,stream=True)) as response:
            if goodResponse(response):
                return response.content;
            else:
                return None;
    except RequestException as Ex:
        logError("Error during requests to {0} : {1}".format(url, str(Ex)));

def goodResponse(_response):
    contentType = _response.headers["Content-Type"].lower();
    return (_response.status_code == 200 and contentType is not None and contentType.find("html") > -1);

def logError(errorResponse):
    print(errorResponse);


#print(getURL(URL));
#raw_html = open(getURL(URL)).read();
#html = BeautifulSoup(getURL(URL), "html.parser");
#client = uReq(URL);
#soup = BeautifulSoup(client.read(), 'html.parser');
browser = webdriver.PhantomJS();
browser.get(URL);
html = browser.page_source;
soup = BeautifulSoup(html, "lxml");
#soup = BeautifulSoup(getURL(URL), "html.parser");
#for p in html.select('p'):
for span in soup.select('span'):
    #if(span['class'] == 'st_1QzH2P8 st_8u0ePN3'):
    try:
        #if span['class'] == "st_1QzH2P8 st_8u0ePN3":
        for data in span['class']:
            if data == "st_8u0ePN3":
                print(span.contents);
                print("Found data!");
            #print(data);
        #if span['class'] == "st_8u0ePN3":
            #print(span.text);
            #print("Found span");
        #print(span["class"]);
        #print("Searching");
    #except:
    except(AttributeError, KeyError) as er:
        logError("Failed Except");
        pass;
