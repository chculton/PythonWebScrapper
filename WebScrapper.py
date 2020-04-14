from requests import get;
from requests.exceptions import RequestException;
from contextlib import closing;
from bs4 import BeautifulSoup;

def getURL(url):
    try:
        with closing(get(url,stream=true)) as response:
            if goodResponse(response):
                return response.content;
            else:
                return None;
    except RequestException as Ex:
        log_error("Error during requests to {0} : {1}".format(url, str(Ex)));

def goodResponse(_response):
    contentType = _response.headers["Content-Type"].lower();
    return (_response.status_code == 200 and contentType is not None and contentType.find("html") > -1);
