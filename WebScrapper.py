# External Libraries
#from requests import get;
#from requests.exceptions import RequestException;
from contextlib import closing;
from bs4 import BeautifulSoup;
from selenium import webdriver;

# Python Libraries
import os;

# Local files
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

# Function Definitions
#def getURL(url):
#    try:
#        with closing(get(url,stream=True)) as response:
#            if goodResponse(response):
#                return response.content;
#            else:
#                return None;
#    except RequestException as Ex:
#        logError("Error during requests to {0} : {1}".format(url, str(Ex)));

#def goodResponse(_response):
#    contentType = _response.headers["Content-Type"].lower();
#    return (_response.status_code == 200 and contentType is not None and contentType.find("html") > -1);

def logError(errorResponse):
    print(errorResponse);

def establishHeadlessFirefox():
     firefoxOptions = webdriver.FirefoxOptions();
     firefoxOptions.add_argument('--headless');
     return webdriver.Firefox(options=firefoxOptions, service_log_path=localDirectory+"\\geckodriver.log");

# MAIN
browser = establishHeadlessFirefox();
browser.get(URL);
soup = BeautifulSoup(browser.page_source, "html.parser");

#tickerStorage = [[],[]];
tickerDetailsStorage = [["first", "row"], ["Second", "row"]];
ticker = 0;
tickerDetails = 0;

for span in soup.select('span'):
    try:
        #if span['class'] == "st_1QzH2P8 st_8u0ePN3":
        rowOfData = ["why", "work"];
        for data in span['class']:
            if data == "st_8u0ePN3":
                # the content prints as ticker, price, point increase, then percentage increase
                print(span.text);
                rowOfData.append(span.text);
                #tickerStorage[ticker][tickerDetails] = span.text;
                #tickerStorage[ticker][tickerDetails].append(span.text);
                tickerDetails += 1;


                #print(span.contents);
                #print("Found data!");
            #print(data);
        #if span['class'] == "st_8u0ePN3":
            #print(span.text);S
            #print("Found span");
        #print(span["class"]);
        #print("Searching");
        tickerDetailsStorage.append(rowOfData);
        tickerDetails = 0;
        ticker += 1;
    except:
    #except(AttributeError, KeyError) as er:
        logError("Span did not contain a class tag");
        pass;

print(tickerDetailsStorage);
#for a in range(len(tickerStorage)):
#    for s in range(len(tickerStorage[a])):
#        print(tickerStorage[a][s], end=' ')
#    print()

# Closes the browser
browser.quit();
