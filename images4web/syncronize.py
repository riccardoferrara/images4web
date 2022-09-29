from folder import *
from PIL import Image
from os import path, remove

class Syncronize:
    def __init__(self, inputFolderPath, outputFolderPath):
        self.InputFolder = InputFolder(inputFolderPath)
        self.OutputFolder = OutputFolder(outputFolderPath)
        self.what2sync()
        self.syncCompress()
        self.syncDelete()

    def syncCompress(self):
        if len(self.loi2sync) == 0:
            return
        else:
            print('\nCompress images from folder %s:' % self.InputFolder.path)
            for i in self.loi2sync:
                self.compressImage(
                    path.join(self.InputFolder.path, i),
                    path.join(self.OutputFolder.path, i)
                )
                print('%s compressed' % i)

    def syncDelete(self):
        if len(self.loi2del) == 0:
            return
        else:
            print('\nDelete images from folder %s:' % self.OutputFolder.path)
            for i in self.loi2sync:
                remove(path.join(self.OutputFolder.path, i))

    def what2sync(self):
        self.loi2sync = []
        self.loi2del = []
        self.loi2sync = list(set(self.InputFolder.loi) - set(self.OutputFolder.loi))
        self.loi2del = list(set(self.OutputFolder.loi) - set(self.InputFolder.loi))
    
    def compressImage(self, imagePath, outputImagePath):
        Im = Image.open(imagePath)
        Im.save(outputImagePath, optimize=True, quality=30) 

