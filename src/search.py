
from collections import OrderedDict
import requests
from bs4 import BeautifulSoup
import sys, tempfile, os
from subprocess import call
from api import client_id,client_secret,key
import curses


class Search:

    def __init__(self, query):

        try:
            self.query = query[0]
            self.tags = query[1]
        except:
            self.query = query
            self.tags = ''
        
        
        self.results = OrderedDict()
        self.initilizeSearch()
        self.search()

        

    def initilizeSearch(self):
        BASEURL = "https://api.stackexchange.com/search/advanced"
        params = {
        "site" : "stackoverflow",
        "key" : key,
        "q" : self.query,
        "tagged" : self.tags
        
        }
        try:
            self.jsonRes = requests.get(BASEURL, params=params, timeout=10).json()
        except Exception as e:
            print(e)
        finally:
            curses.initscr().scrollok(False)
            curses.initscr().keypad(False)
            curses.endwin()
            exit()
            
        

    
    def search(self):

        for items in self.jsonRes['items']:
            if(items['is_answered'] == True):
                self.results[items['title']] = items["link"]
          
        if len(self.results) == 0:
            return "None"

        return
    

    def scrape(self,choiceLink):
        link = requests.get(choiceLink)

        soup = BeautifulSoup(link.content,'html.parser')
        retList = []
        
        for body in soup.find_all("div", class_ = "s-prose js-post-body"):
            retList.append(str(body.getText()))

        return retList
        
    def returnListOfTitles(self):
        return list(self.results.keys())
    
    def displayQuestionsAnswer(self,key):
        link = self.results.get(key)
        paragraph = self.decide(link)
        self.displayAnswer(paragraph)
        return "Done"
    
    def decide(self,link):
    
        answer = self.scrape(link)
        return self.combineParagraphs(answer)

    
    def combineParagraphs(self,answer):
        para = ""
        for paragraphs in answer:
            para += paragraphs

        return para
    
    
    def displayAnswer(self,answer):
        EDITOR = os.environ.get('EDITOR','vim') 

        initial_message = str.encode(answer) 

        with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
            tf.write(initial_message)
            tf.flush()
            call([EDITOR, tf.name])
            tf.close()


        return 
            
    
    
    







