import unittest
import sys
import requests
from requests.models import CONTENT_CHUNK_SIZE

sys.path.insert(0,'/Users/oscargandara/overflow/src')

import MenuController as MC 

type1 = "ErrorMenu"
type2 = "ChoiceMenu"
type3 = "KeywordMenu"
type4 = "SearchResultsMenu"
errors = ["Error 1","Error 2","Error 3","Error 4", "Error 5"]  


QUESTION_OPTION = ["Would you like to add keywords?", "Yes", "No"]
keywords = ["Key 1", "Key 2", "Key 3", "Key 4"] 

class testController(unittest.TestCase):

    def setUp(self):
       
        self.controller = MC.MenuController(errors)
    
    def tearDown(self):
        print("Test Done")
        self.controller = MC.MenuController(errors)

    def testErrorMenu(self):
        self.assertListEqual(self.controller.menu.menu, errors)
    
    
    def testFactoryCallAfterErrorMenu(self):
        self.controller.chooseMenu(errors[0])
        self.assertEqual(self.controller.menu.menuType(),type2)
        self.assertEqual(self.controller.menu.query[-1],errors[0])
        self.assertListEqual(self.controller.menu.menu, QUESTION_OPTION)
    
    
    def testFactoryCallAfterTest1(self):
        self.controller.chooseMenu(errors[1])
        self.controller.chooseMenu("No")
        self.assertEqual(self.controller.menu.menuType(), "SearchResultsMenu")
        self.assertEqual(self.controller.menu.query[-1],errors[1])
        self.assertEqual(len(self.controller.previousMenu),2)
    
    def testFactoryCallAfterTest2(self):
        
        self.controller.chooseMenu(errors[1])
        self.controller.chooseMenu("Yes")
        self.assertEqual(self.controller.menu.type, "KeywordMenu")
        #print(self.controller.menu.query)
    
    
    def testFactoryCallAfterTest3(self):
        
        self.controller.chooseMenu("Error 2")
        self.controller.chooseMenu("Yes")
        self.controller.chooseMenu(keywords)

        self.assertEqual(self.controller.menu.type, "SearchResultsMenu")
        self.assertListEqual(self.controller.menu.query[-1],keywords)
        self.assertEqual(len(self.controller.previousMenu),3)
        #print(self.controller.menu.query)
   
   
    
    def testpressESCAfterTest4(self):
        
        self.controller.chooseMenu("Error 2")
        self.controller.chooseMenu("Yes")
        self.controller.chooseMenu(keywords)
        self.controller.pressESC()
        self.assertEqual(self.controller.menu.type, "ChoiceMenu")
        self.assertEqual(len(self.controller.previousMenu),1)
        self.assertEqual(len(self.controller.menu.query),1)
    
    
    
    def testStartOverToErrorMenu(self):
        self.controller.chooseMenu("Error 2")
        self.controller.chooseMenu("Yes")
        self.controller.chooseMenu(keywords)
        self.controller.pressESC()
        print("query:" ,self.controller.menu.query)
        self.controller.pressESC()
        self.assertEqual(self.controller.menu.type, "ErrorMenu")
        self.assertListEqual(self.controller.menu.menu, errors)
        self.assertEqual(len(self.controller.previousMenu),0)

    
    
    def testChangingError(self):
        self.controller.chooseMenu("Error 2")
        self.controller.chooseMenu("Yes")
        self.controller.chooseMenu(keywords)
        self.controller.pressESC()
        
        self.controller.pressESC()

        self.assertEqual(len(self.controller.menu.query),0)
        self.controller.chooseMenu("Error 3")
        self.assertEqual(self.controller.menu.type, "ChoiceMenu")
        self.assertEqual(self.controller.menu.query[-1],"Error 3")
    
    
    def testChangingtoNoKeywords(self):

        self.controller.chooseMenu("Error 2")
        self.controller.chooseMenu("Yes")
        self.controller.chooseMenu(keywords)
        self.controller.pressESC()

        #print(self.controller.menu.type)
        
        self.controller.chooseMenu("No")

        self.assertEqual(self.controller.menu.type, "SearchResultsMenu")
        self.assertEqual(self.controller.menu.query[-1],"Error 2")

    
    def testChangingKeywords(self):

        differentKeywords = ['One','Two','Three']
        self.controller.chooseMenu("Error 2")
        self.controller.chooseMenu("Yes")
        self.controller.chooseMenu(keywords)
        self.assertListEqual(self.controller.menu.query[-1],keywords)
        self.controller.pressESC()

        self.controller.chooseMenu("Yes")
        self.controller.chooseMenu(differentKeywords)

        self.assertEqual(self.controller.menu.type, "SearchResultsMenu")
        print(self.controller.menu.query)
        self.assertListEqual(self.controller.menu.query[-1],differentKeywords)

    
    def testCompleteExit(self):
        print(self.controller.pressESC())

        self.assertEqual(len(self.controller.menu.query),0)

    











        

    
    