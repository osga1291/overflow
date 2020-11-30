import sys
import logging
import subprocess
import tempfile
import time
import curses
import gui 
import tkinter as tk 
logging.basicConfig(filename='test.log')

error_type = ["AssertionError", "AttributeError","EOFError","FloatingPointError","GenerationExit","ImportError","IndexError",
"KeyError","KeyboardError","MemoryError","NameError","NotImplementedError","OSError","OverflowError","ReferenceError","StopIteration",
"SyntaxError","IndentationError","TabError","SystemError","SystemExit","TypeError","UnboundLocalError","UnicodeError",
"UnicodeEncodeError","UnicodeDecodeError","UnicodeTranslateError","ValueError","ZeroDivisionError"]


def execute(arr):
    
    execGUI = gui.Menu(1,arr)
    curses.wrapper(execGUI.gui())
        
    return


    

def main():
    logger = logging.getLogger()

    logger.setLevel(logging.DEBUG)

    
    try:
        inFile = sys.argv[1]
        arg = "./" + str(inFile)
        exec(open(arg).read())
        return 1
       

    except Exception as e:
        logging.error("Exception occured", exc_info=True)
        arr =[]
        with open('test.log','r') as inFile:
            for line in inFile:
                for error in error_type:
                    if error in line:
                        arr.append(line)
        with open('test.log', 'w') as outFile:
            outFile.write('')
        

        
        execute(arr)

       


        
        


    
   


    
if __name__ == "__main__":
    main()