import Menus as M

class Menufactory():
    QUESTION_OPTION = ["Would you like to add keywords?", "Yes", "No"]
    
    def __init__(self):
        pass

    def createMenu(self, menu: M.Menu, choice):


        if menu.menuType() == "ErrorMenu": 
            return M.ChoiceMenu(choice,Menufactory.QUESTION_OPTION)
        
        elif menu.menuType() == "ChoiceMenu":
            if (choice == "Yes"):
                return M.KeywordMenu()
            else: 
               return M.SearchResultsMenu() 
        
        elif menu.menuType() == "KeywordMenu": 
            return M.SearchResultsMenu(choice) 
       
        elif menu.menuType() == "SearchResultsMenu":
            menu.usersChoice(choice)
            return menu
        
        else:
            return M.ErrorMenu(choice)
        
        
    