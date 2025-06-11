import requests
import selectorlib   #extract the HTML code
from datetime import datetime
import sqlite3


URL = "http://programmer100.pythonanywhere.com/"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}   
#HEADERS tell the web server that this script is actually a web browser !!!IMPORTANT TO WRITE HERE!!!
sql_connection = sqlite3.connect("data.db")

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
# def store(extracted):
#    now = datetime.now().strftime("%y-%m-%H-%M-%S")
#    with open("date.txt", 'a') as file:
#       line = f"{now}, {extracted}\n"
#       file.write(line)
#stores the data in the database
def store(extracted):
    row = datetime.now().strftime("%y-%m-%H-%M-%S")
    cursor = sql_connection.cursor()
    cursor.execute("INSERT INTO temperatures VALUES (?, ?)", (row, extracted))
    sql_connection.commit()  #commit the changes to the database

#reads the db
def read(extracted):
   row = extracted.split(",")
   row = [item.strip() for item in row] #strip the spaces
   date, temperature = row
   cursor = sql_connection.cursor()
   cursor.execute("SELECT * FROM temeperatures WHERE date = ? AND temperature = ?", (date, temperature))
   rows = cursor.fetchall() #prints the rows that match the query
   print(rows) 
   return rows


if __name__ == "__main__":
    
    scraped = scrape(URL)
    extracted =  extract(scraped)
    print(extracted)
    store(extracted) #store the data only when it's new 
            
   