import logging


class ErrorCatcher():

    def __init__(self):



        logging.basicConfig(filename='test.log')

        self.error_type = ["AssertionError", "AttributeError","EOFError","FloatingPointError","GenerationExit","ImportError","IndexError",
            "KeyError","KeyboardError","MemoryError","NameError","NotImplementedError","OSError","OverflowError","ReferenceError","StopIteration",
            "SyntaxError","IndentationError","TabError","SystemError","SystemExit","TypeError","UnboundLocalError","UnicodeError",
            "UnicodeEncodeError","UnicodeDecodeError","UnicodeTranslateError","ValueError","ZeroDivisionError"]
        
        self.arrayOfErrors = []
        self.writeLogErrors()
        self.ReadErrorsFound()
        #self.clearLogPage()

    def getArrayOfErrors(self):
        return self.arrayOfErrors
    
    def writeLogErrors(self):
        logging.error("Exception occured", exc_info=True)

    def ReadErrorsFound(self):

        with open('test.log','r') as logFile:
            for line in logFile:
                for error in self.error_type:
                    if error in line:
                        self.arrayOfErrors.append(line)

    def clearLogPage(self):
        with open('test.log', 'w') as outFile:
            outFile.write('')

    


