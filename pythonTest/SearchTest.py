import unittest
import sys


sys.path.insert(0,'/Users/oscargandara/overflow/src')

from search import Search


class testSearch(unittest.TestCase):

    
    def testInitlizeWithoutParams(self):
        
        search  = Search("ImportError: No module named")
        self.assertNotEqual(len(search.results),0)
        print(search.results)

    def testInitilizeWithParams(self):
        search = Search(["Exception in thread mainjava.lang.ArrayIndexOutOfBoundsException:","recursion","java"])
        self.assertNotEqual(len(search.results),0)
        print(search.results)
    

    def testScraping(self):
        search = Search(["Exception in thread mainjava.lang.ArrayIndexOutOfBoundsException:","recursion","java"])
        lst = search.decide(1)
        self.assertNotEqual(len(lst),0)
        
    '''
    
    def testDisplay(self):
        search = Search(["Exception in thread mainjava.lang.ArrayIndexOutOfBoundsException:","recursion","java"])
        lst = search.decide(0)
        self.assertIsInstance(lst,str)
        search.displayAnswer(lst)
    '''


