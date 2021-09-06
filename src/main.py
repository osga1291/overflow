from Menus import ErrorMenu
import sys
import logging
import gui
from ErrorCatcher import ErrorCatcher


class ProgramExecutor():

    def __init__(self):
        self.errorList = []
        self.catchErrors()
        self.executeProgram()

           
    def executeStackOverFlow(self):

        gui.gui(self.errorList)

        
       

    def executePythonFile(self):
        inFile = sys.argv[1]
        arg = "./" + str(inFile)
        exec(open(arg).read())


    def catchErrors(self):

        logger = logging.getLogger()
        logger.setLevel(logging.WARNING)

        try:
            self.executePythonFile()
              
        except Exception:
            
            errorObject = ErrorCatcher()
            self.errorList = errorObject.getArrayOfErrors()
               
    
    def executeProgram(self):
        if(len(self.errorList) != 0):
            self.executeStackOverFlow()
        print("The Python program does not contain errors.")

def main():

    ProgramExecutor()


    

       


        
        


    
   


    
if __name__ == "__main__":
    main()