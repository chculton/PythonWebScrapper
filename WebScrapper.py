# External Libraries
#from requests import get;
#from requests.exceptions import RequestException;
from contextlib import closing;
from bs4 import BeautifulSoup;
from selenium import webdriver;
import numpy as np;

import time;

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
     # UNCOMMENT FOR HEADLESS BROWSER
     firefoxOptions.add_argument('--headless');
     return webdriver.Firefox(options=firefoxOptions, service_log_path=localDirectory+"\\geckodriver.log");

# MAIN
browser = establishHeadlessFirefox();
browser.get(URL);
# seems that there is a maximum amount of html that can be returned
# parsing the python seems to parse the same amount of code as
# previously, just now its the last 16 stocks, rather than the prior 17
#time.sleep(5);
soup = BeautifulSoup(browser.page_source, "html.parser");
# Closes the browser
browser.quit();

#tickerStorage = [[],[]];
#tickerDetailsStorage = [["first", "row"], ["Second", "row"]];
#tickerDetailsStorage = np.array();
ticker = 0;
tickerDetails = 0;
rowOfData = [];

isPositive = False;
for span in soup.select('span'):
    try:
        #if span['class'] == "st_1QzH2P8 st_8u0ePN3":
        for data in span['class']: #this essentially looks through all spans
            if data == "st_w-QlNFW":
                isPositive = True;
                rowOfData.append(" Positive");
            if data == "st_37VuZWc":
                rowOfData.append(" Negative");
            if data == "st_8u0ePN3":
                #try:
                #    for searchForColor in data.contents:
                #        if searchForColor == "st_2fTou_q":
                #            rowOfData.append("Positive");
                #        else:
                #            rowOfData.append("Negative");
                #except:
                #    print("Can't find color.");
                # the content prints as ticker, price, point increase, then percentage increase
                if span.text:
                    rowOfData.append(span.text);
                    #if(isPositive):
                    #    rowOfData.append("Positive");
                    #    isPositive = False;
                    #else: rowOfData.append("Negative");

                tickerDetails += 1;
        tickerDetails = 0;
        ticker += 1;
    except:
        #logError("Span did not contain a class tag");
        pass;

dataToSave = np.array(rowOfData);
index = [0];
newArray = np.delete(dataToSave, index);

stockInfoString = "";

stockInformation = [];
for i in range(len(newArray)):
    #if i%3 == 0:
    if i%4 == 0 and i != 0:
        stockInformation.append(stockInfoString);
        stockInfoString = "";
    tempString2 = newArray[i];
    if(len(tempString2.split()) > 1):
        newTempArray = tempString2.split();
        stockInfoString += newTempArray[0] + " " + newTempArray[1];
    else:
        stockInfoString += tempString2 + " ";

for k in range(len(stockInformation)):
    print(str(k) + " entry in stock info: " + stockInformation[k]);
