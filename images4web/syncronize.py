from folder import *

class Syncronize:
    def __init__(self, inputFolderPath, outputFolderPath):
        self.InputFolder = InputFolder(inputFolderPath)
        self.OutputFolder = OutputFolder(outputFolderPath)
