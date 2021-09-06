import MenuFactory as MF 
import Menus as Menu
    
class MenuController:   

    def __init__(self,array):
        self.previousMenu = []
        self.MenuFactory = MF.Menufactory() 
        self.menu = Menu.ErrorMenu(array)   
    
    def addMenuToStack(self):
        self.previousMenu.append(self.menu)

    
    def chooseMenu(self, choice): 
        if (self.menu.menuType() != "KeywordMenu"):
            choice = self.menu.menu[choice]
        
        newMenu = self.MenuFactory.createMenu(self.menu,choice)
        if (self.menu.menuType() != "SearchResultsMenu"):
            self.addMenuToStack()
        self.menu = newMenu
        
    
    def exitMenu(self):
        if (self.menu.type == "SearchResultsMenu"):
            self.menu = self.previousMenu[-2] 
            self.previousMenu.pop()
            self.previousMenu.pop()
        else:
            self.menu = self.previousMenu[-1]
            self.previousMenu.pop()

    
    def pressESC(self):
        if (len(self.previousMenu) > 0):
            self.exitMenu()  
            return        
        else:
            print("Exit")
            return "Exit"
