from search import Search 
    
class Menu:
    query = []
    def __init__(self,array = None):
        self.type = "None"
        self.menu = array
    
    def returnMenu(self):
        if(self.type == "KeywordMenu"):
            pass
        else:
            if(len(self.query) != 0):
                self.query.pop()

    def menuQuery(self):
        return self.query

    def menuType(self):
        return self.type

    def menuSize(self):
        return len(self.menu)
    
    def __del__(self):
        self.returnMenu()

class ErrorMenu(Menu):
    def __init__(self,array):
        super().__init__()
        self.menu = array
        self.type = "ErrorMenu"
        
class ChoiceMenu(Menu):
    def __init__(self,choice,array):
        super().__init__()
        self.menu = array
        self.type = "ChoiceMenu" 
        Menu.query.append(choice)


class KeywordMenu(Menu):

    def __init__(self):
        super().__init__()
        self.type = "KeywordMenu"   

class SearchResultsMenu(Menu):
    def __init__(self,array = None):
        super().__init__(array)
        self.type = "SearchResultsMenu"

        if array != None:
            
            Menu.query.append(array)
        self.getSearchResults()

    def getSearchResults(self):
        self.search = Search(Menu.query)
        self.menu = self.search.returnListOfTitles()
        
    def usersChoice(self,count):
        self.search.displayQuestionsAnswer(count)
    