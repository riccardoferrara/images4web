from images4web.syncronize import Syncronize
from images4web import compress
import os
import unittest
from files import files
import filecmp

outputImagesFolderPath = 'tests/images/.compressed4web' #folder that will contain images after compression
inputImagesFolderPath = 'tests/images' #folder containing input images for test
templateImagesFolderPath = 'tests/images/templateCompressedImages'#folder containing images already compressed (for comp. test)
inputImageFilePath = 'tests/images/1.JPG' #1st test image
outputImageFilePath = 'tests/images/.compressed4web/1.JPG' #path of the 1st output image after compression
templateImageFilePath = 'tests/images/templateCompressedImages/1.JPG' #template of already compressed image (for comp. test)
compressionQuality = 10 # images already compressed in the template folder are compressed at 10, if you change test will ko
numberOfTestImages = 8 #number of images inside the input folder

class compressTenTemplateImages(unittest.TestCase):
    def test_compress_an_image(self):
        files.deleteAllFilesInFolder(outputImagesFolderPath)
        compress.compressImage(inputImageFilePath, outputImageFilePath, compressionQuality)
        self.assertTrue(filecmp.cmp(outputImageFilePath, templateImageFilePath))
        files.deleteAllFilesInFolder(outputImagesFolderPath)

    def test_compress_all_images_in_folder(self):
        files.deleteAllFilesInFolder(outputImagesFolderPath)
        Sync1 = Syncronize(inputImagesFolderPath, outputImagesFolderPath, compressionQuality=10)
        self.assertTrue(len(os.listdir(outputImagesFolderPath)) >= numberOfTestImages)
        for i in range(1,9):
            outputImagePath = os.path.join(outputImagesFolderPath, (str(i) + '.JPG'))
            templateImagePath = os.path.join(templateImagesFolderPath, (str(i) + '.JPG'))
            self.assertTrue(filecmp.cmp(outputImagePath, templateImagePath)) 
        files.deleteAllFilesInFolder(outputImagesFolderPath)


if __name__ == '__main__':
    unittest.main()
