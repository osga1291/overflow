from os import name
from MenuController import MenuController
import curses

class gui:

    def __init__(self,array):
        self.stdscr = curses.initscr()
        self.initlizeCurses()
        self.MenuController = MenuController(array)
        self.gui()
        
    def initlizeCurses(self):   
        
        self.stdscr.keypad(True)
        self.stdscr.scrollok(True)
        curses.curs_set(0)
        curses.start_color()
        curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_WHITE)  
                 
    def getKey(self):
        key = self.stdscr.getch()
        self.stdscr.clear()
        return key
        
    def actionForKey(self,key):
        
        if key == curses.KEY_UP and self.current_row_index > 0:
            self.current_row_index -= 1
        elif key == curses.KEY_DOWN and self.current_row_index < len(self.MenuController.menu.menu)-1:
            self.current_row_index += 1
        elif key == curses.KEY_ENTER or key in [10,13]:
            self.MenuController.chooseMenu(self.current_row_index)
            self.gui()
        elif key == 27:
            flag = self.MenuController.pressESC()
            if(flag):
                self.exitProgram()
        
 
    def guiForKeywordMenu(self):
        self.printKeywordMenu()
        return self.getKeyWord()
        
    def gui(self):
        if (self.MenuController.menu.type == "KeywordMenu"):
            input_char = self.guiForKeywordMenu()   
            self.MenuController.chooseMenu(input_char)
            
        curses.wrapper(self.guiForArrayMenu())
    
    def guiForArrayMenu(self):

        self.initlizeCurses()
        
        self.current_row_index = 0
        self.printArrayMenu()
        while 1:
            keyUsed = self.getKey()
            self.actionForKey(keyUsed)
            self.refreshAfterMoving()
            
    def refreshAfterMoving(self):
        self.printArrayMenu()
        self.stdscr.refresh()
    
    def printArrayMenu(self):

        self.stdscr.clear()
        h,w = self.stdscr.getmaxyx()
        for idx, row in enumerate(self.MenuController.menu.menu):
            x = w//2 - len(row)//2
            y = h//2 - len(self.MenuController.menu.menu)//2 + idx
            if idx == self.current_row_index:
                self.stdscr.attron(curses.color_pair(1))
                try:
                    self.stdscr.addstr(y,x,row)
                except:
                    pass
                self.stdscr.attroff(curses.color_pair(1))
            else:
                try:
                    self.stdscr.addstr(y,x,row)
                except:
                    pass
        self.stdscr.refresh() 

    def printKeywordMenu(self):
        self.stdscr.clear()
        curses.echo()
        self.stdscr.addstr(0,0,"Type your keywords:")
        self.stdscr.refresh()   

    def getKeyWord(self):
    
        input_char = self.stdscr.getstr(1,0,100).decode(encoding="utf-8")
        self.stdscr.clear()
        self.stdscr.refresh()

        return input_char.split()
               
    def exitProgram(self):

        self.stdscr.scrollok(False)
        self.stdscr.keypad(False)
        curses.endwin()
        exit()


'''
def main():
    errorList = ["ImportError: No module named", "Exception in thread mainjava.lang.ArrayIndexOutOfBoundsException:"]
    try:
        
        
        gui(errorList)
    
    except Exception as e:
        curses.initscr().scrollok(False)
        curses.initscr().keypad(False)
        curses.endwin()
        print(e)
        exit()
    finally:
        print('Hello')


if __name__ == '__main__':
    main()
'''

        
    



        
    
        
    

    
    
    

