import curses
import time
from collections import OrderedDict 
import search


class Menu:
    string = []
    def __init__(self,type_menu, array):
        self.menu = array
        self.type = type_menu
        self.stdscr = curses.initscr()
        self.stack = []
        self.searchResults = OrderedDict()
        
        
        




    def print_menu(self,current_row_ind):
        self.stdscr.clear()
        h,w = self.stdscr.getmaxyx()
        for idx, row in enumerate(self.menu):
            x = w//2 - len(row)//2
            y = h//2 - len(self.menu)//2 + idx
            if idx == current_row_ind:
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
        return



    def gui(self):
        self.stdscr.keypad(True)
        self.stdscr.scrollok(True)
        curses.curs_set(0)
        curses.start_color()
        curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_WHITE)
                
        current_row_ind = 0
        self.print_menu(current_row_ind)
            
        while 1:
            key = self.stdscr.getch()
            self.stdscr.clear()
                
                

            if key == curses.KEY_UP and current_row_ind > 0:
                current_row_ind -= 1
            elif key == curses.KEY_DOWN and current_row_ind < len(self.menu)-1:
                current_row_ind += 1
            elif key == curses.KEY_ENTER or key in [10,13]:

                if self.type == 1:
                    Menu.string.append(str(self.menu[current_row_ind]))
                
                    self.stdscr.refresh()
                    newMenu = Menu(0,["Would you like to add keywords?", "Yes", "No"])
                    newMenu.stack.append(self)
                    curses.wrapper(newMenu.gui())
                

                elif self.type == 0:
                    if self.menu[current_row_ind] == "Yes":
                        self.inputKeyWords()
                        self.startSearch()
                       
                    else:
                        self.startSearch()

                else:
                    self.getAnswer(self.searchResults,current_row_ind)
                    curses.wrapper(self.gui())
                    
            
            elif key == 27:
                self.exitMenu()
            
              
                 
            self.print_menu(current_row_ind)
            self.stdscr.refresh()

    def exitMenu(self):
        if (len(self.stack) > 0):
            self.stack.pop().gui()
                    
        else: 
            self.stdscr.scrollok(False)
            self.stdscr.keypad(False)
            curses.endwin()
            exit()

        
    def inputKeyWords(self):
        self.stdscr.clear()
        curses.echo()
        
        self.stdscr.addstr(0,0,"Type your keywords:")
        self.stdscr.refresh()
        input_char = self.stdscr.getstr(1,0,100).decode(encoding="utf-8")
        self.stdscr.clear()
        self.stdscr.refresh()
        Menu.string.append(input_char)
        return 

    def startSearch(self):
        results = search.search_stack(self)
        searchMenu = Menu(3,results)
        searchMenu.searchResults = results
        searchMenu.stack.append(self)
        curses.wrapper(searchMenu.gui())
        return 

    def getAnswer(self,searchResults,count):

        answer = search.decide(searchResults,count)
        retString = " ".join(answer)
        search.displayAnswer(retString)

        return



       




        
    



        
    
        
    

    
    
    

