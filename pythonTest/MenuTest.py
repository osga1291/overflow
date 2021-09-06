import sys
import os
import unittest


sys.path.remove('/Users/oscargandara/overflow/pythonTest/Users/oscargandara/overflow/src')
sys.path.insert(0,'/Users/oscargandara/overflow/src')

import MenuFactory as MF
import Menus as M


type1 = "ErrorMenu"
type2 = "ChoiceMenu"
type3 = "KeywordMenu"
type4 = "SearchResultsMenu"

QUESTION_OPTION = ["Would you like to add keywords?", "Yes", "No"]

choice_menu = ["Would you like to add keywords?", "Yes", "No"]
error_menu = ["Error 1", "Error 2", "Error 3"]

class testCreation(unittest.TestCase):


    
    def setUp(self):
        self.menu = M.ErrorMenu(error_menu)
        self.factory = MF.Menufactory()

    def tearDown(self):
        self.menu = M.ErrorMenu(error_menu)
    
    def testCreationType1(self):

        actual = self.factory.createMenu(self.menu,error_menu[0])
        self.assertEqual(actual.menuType(),type2)
    
    def testCreationType2No(self):
        self.menu = self.factory.createMenu(self.menu,error_menu[0])
        self.menu = self.factory.createMenu(self.menu, choice_menu[2])
        self.assertEqual(self.menu.menuType(),type4)
    

    def testCreationType2Yes(self):
        self.menu = self.factory.createMenu(self.menu,error_menu[0])
        self.menu = self.factory.createMenu(self.menu, choice_menu[1])
        self.assertEqual(self.menu.menuType(), type3)
    
    def testCreationKeywordToSearch(self):
        keyList = ["Key1","Key2","Key3"]
        self.menu = self.factory.createMenu(self.menu,error_menu[0])
        self.menu = self.factory.createMenu(self.menu, choice_menu[1])
        self.menu = self.factory.createMenu(self.menu, keyList) 
        self.assertEqual(self.menu.menuType(), type4)
        self.assertNotEqual(self.menu.menuSize(), 0)
    
    def testScrapingAndDisplayAnswer(self):

        keyList = ["Key1","Key2","Key3"]
        self.menu = self.factory.createMenu(self.menu,error_menu[0])
        self.menu = self.factory.createMenu(self.menu, choice_menu[1])
        self.menu = self.factory.createMenu(self.menu, keyList) 
        actual = self.factory.createMenu(self.menu,1)
        self.assertEqual(actual.menuType(),self.menu.menuType())




if __name__ == "__main__":
    unittest.main()