<div align="center"> <h1>Python Web Scrapper</h1> </div>
            
> A Python web scriping program which reads from a txt file what details to scrape for and what website to visit, then returning the results in a new txt file.

> Developed by C. Hans Culton

> Apache-2.0

## Libraries
- BeautifulSoup4
- Selenium
- Firefox

## How to Use
Download the project. Enter the URL into the txt file, URLToScrape.txt. Add elements you would like to scrape for to the same txt file. Run the python file, and a new file, results.txt, will be created in the same directory, populated with the results of the scrape.

## Default URL and Why
<div>
<p>Initially this project visits <a href="https://stocktwits.com/discover/earnings-calendar/">Stocktwits</a></p>
            <p>https://stocktwits.com/discover/earnings-calendar/</p>
            <p>I chose this website as it is heavily reliant off of AJAX requests and JavaScript, making it challenging to scrape information from. Furthermore, it has unique and changing content everyday, making for an interesting website to scrape. The URL to visit, however, can be changed in the URLToScrape.txt.
            </div>
