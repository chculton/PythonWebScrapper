# Python Libraries
import os;
import time;
import numpy as np;

# External Libraries
from contextlib import closing;
from bs4 import BeautifulSoup;
from selenium import webdriver;
from selenium.webdriver.support.ui import WebDriverWait;

# Local files
import TxtParser;

# Function Definitions
def logError(errorResponse):
    print(errorResponse);

def establishHeadlessFirefox():
     firefoxOptions = webdriver.FirefoxOptions();
     # UNCOMMENT FOR HEADLESS BROWSER
     firefoxOptions.add_argument('--headless');
     return webdriver.Firefox(options=firefoxOptions, service_log_path=localDirectory+"\\geckodriver.log");

# seems that there is a maximum amount of html that can be returned
# parsing the python seems to parse the same amount of code as
# previously, just now its the last 16 stocks, rather than the prior 17
#time.sleep(5);
def findTickers():
    soup = BeautifulSoup(browser.page_source, "html.parser");
    #print(soup)
    # Closes the browser
    #browser.quit();

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

def scrollPage(_xScrollAmountInPixels, _yScrollAmountInPixels):
    browserCommand = "window.scrollBy(" + str(_xScrollAmountInPixels) + "," + str(_yScrollAmountInPixels) + ")"
    for i in range(2):
        browser.execute_script(browserCommand)
        findTickers()
        time.sleep(2)

# Scroll down the page
def scrollToPageBottom():
    k = 0;
    currentPage = browser.page_source
    while (k < 2):
        scrollPage(0, 500)
        scrolledPage = browser.page_source
        if scrolledPage != currentPage:
            currentPage = scrolledPage
            k = 0;
        else:
            # if this happens 2 in a row, page bottom had been met
            # close the browser window
            k += 1;
            break

# MAIN
# Initialize storage for parsed file data
textFileData = [];

# Get local directory
localDirectory = os.path.dirname(os.path.realpath(__file__));
fileToReadPath = localDirectory+"\\URLToScrape.txt";

# temporary, as this value will be read from a txt file
textFileData = TxtParser.parseFile(fileToReadPath);
URL = textFileData[0];

browser = establishHeadlessFirefox();
browser.get(URL);
scrollToPageBottom();
# Closes the browser
browser.quit();
