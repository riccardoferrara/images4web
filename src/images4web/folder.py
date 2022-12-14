from files import files

imagesExtensions = ['png', 'jpg', 'jpeg', 'tiff']

class Folder():
    def __init__(self, path):
        self.path = path

    def getListOfFiles(self):
        # get the list of files inside the folder
        self.lof = files.getAllFileNamesInDir(self.path)
        self.lof = files.ignoreFilesWithLeftExtension(self.lof, '.')
        return self.lof

    def getListOfImages(self):
        # get the list of images inside the folder
        self.loi = []
        if len(self.lof) == 0:
            return self.loi
        for f in self.lof:
            if f.split('.')[-1].lower() in imagesExtensions:
                self.loi.append(f)
        self.loi = files.ignoreFilesWithLeftExtension(self.loi, '.')
        return self.loi
    
    def create(self):
        files.createDirIfNotExist(self.path)



class OutputFolder(Folder):
    def __init__(self, path):
        super().__init__(path)
        self.create()
        self.type = 'output'
        self.getListOfFiles()
        self.getListOfImages()

class InputFolder(Folder):
    def __init__(self, path):
        super().__init__(path)
        self.type = 'input'
        self.getListOfFiles()
        self.getListOfImages()
    