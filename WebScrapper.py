from requests import get;
from requests.exceptions import RequestException;
from contextlib import closing;
from bs4 import BeautifulSoup;

#from selenium.webdriver import Firefox;
from selenium import webdriver;

import os;

import TxtParser;

# Initialize storage for parsed file data
textFileData = [];

# Get local directory
localDirectory = os.path.dirname(os.path.realpath(__file__));
fileToReadPath = localDirectory+"\\URLToScrape.txt";

# temporary, as this value will be read from a txt file
textFileData = TxtParser.parseFile(fileToReadPath);
URL = textFileData[0];
#URL = "https://stocktwits.com/discover/earnings-calendar/";
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

def establishHeadlessFirefox():
     firefoxOptions = webdriver.FirefoxOptions();
     firefoxOptions.add_argument('--headless');
     return webdriver.Firefox(options=firefoxOptions, service_log_path=localDirectory+"\\geckodriver.log");

#browser = webdriver.Firefox(service_log_path="C:\\Users\\chculton\\AppData\\Local\\Temp\\geckodriver.log");

#browser = webdriver.Firefox(service_log_path="C:\\Users\\chans\\Documents\\Github\\PythonWebScrapper\\geckodriver.log");
browser = establishHeadlessFirefox();

#browser.FirefoxOptions().add_arguement("--headless");

browser.get(URL);
#html = browser.page_source;
soup = BeautifulSoup(browser.page_source, "html.parser");

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
