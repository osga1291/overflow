
from collections import OrderedDict
import requests
from bs4 import BeautifulSoup
import sys, tempfile, os
from subprocess import call
from api import client_id,client_secret,key

def search_stack(Menu):
    query = Menu.string[0]
    tags = ";".join(Menu.string[1:])

    
    BASEURL = "https://api.stackexchange.com/search/advanced"
    params = {
    "site" : "stackoverflow",
    "key" : key,
    "q" : query,
    "tagged" : tags
    
    }
    

    jsonRes = requests.get(BASEURL, params=params).json()

    

    
    
    for items in jsonRes['items']:
        if(items['is_answered'] == True):
            Menu.searchResults[items['title']] = items["link"]
    
    
    if len(Menu.searchResults) == 0:
        return "None"

    return Menu.searchResults
    

def scrape(strLink):
    link = requests.get(strLink)
    soup = BeautifulSoup(link.content,'html.parser')
    retList = []
    
    for body in soup.find_all("div", class_ = "s-prose js-post-body"):
        retList.append(str(body.getText()))

    return retList
    
def decide(searchResults,count):
    
    link = ""
    dictCount = 0
    for key, value in searchResults.items():
        if count == dictCount:
            link = value
            break
        dictCount = dictCount + 1

    answer = scrape(link)
    return answer

    

def displayAnswer(answer):
    EDITOR = os.environ.get('EDITOR','vim') 

    initial_message = str.encode(answer) 

    with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
        tf.write(initial_message)
        tf.flush()
        call([EDITOR, tf.name])
        tf.close()

    return
            

    
    







