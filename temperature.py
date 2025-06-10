import requests
import selectorlib   #extract the HTML code
from datetime import datetime


URL = "http://programmer100.pythonanywhere.com/tours/"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}   
#HEADERS tell the web server that this script is actually a web browser !!!IMPORTANT TO WRITE HERE!!!

def scrape(url):
    """Scrape the page source from URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml") #displaytimer (is a selector) is an id from html page
    value = extractor.extract(source)["tours"] #returns a dictionary with key = tours 
    return value

#stores the data in txt file
def store(extracted):
   now = datetime.now().strftime("%y-%m-%H-%M-%S")
   with open("date.txt", 'a') as file:
      line = f"{now}, {extracted}\n"
      file.write(line)


if __name__ == "__main__":
    
    scraped = scrape(URL)
    extracted =  extract(scraped)
    print(extracted)
    store(extracted) #store the data only when it's new 
            
   