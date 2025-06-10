import requests
import selectorlib   #extract the HTML code
import smtplib, ssl
import os 
import time


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

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "adaflori0207@gmail.com"
    password = "devb uqpp cfxt zbdp"
    
    receiver = "adaflori0207@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
       server.login(username, password)
       server.sendmail(username, receiver, message)

    print("Email was sent!")

#stores the data in txt file
def store(extracted):
   with open("data.txt", 'a') as file:
      file.write(extracted + "\n")


#reads the txt file to see if there are duplicated data
def read(extracted):
   with open("data.txt", 'r') as file:
      return file.read()

if __name__ == "__main__":
   while True:
    scraped = scrape(URL)
    extracted =  extract(scraped)
    print(extracted)
    content = read(extracted)
    if extracted != "No upcoming tours":
        #does not send an email if the email was already sent with the same data
        if extracted not in content:
            store(extracted) #store the data only when it's new 
            send_email(message="Hey, new event was found!")
    time.sleep(2) #runs the script every 2 seconds
