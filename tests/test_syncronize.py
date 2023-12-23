from images4web.syncronize import Syncronize
from images4web import compress
import os
import unittest
from files import files
import filecmp

# folder that will contain images after compression
outputImagesFolderPath = 'tests/images/.compressed4web'
# folder containing input images for test
inputImagesFolderPath = 'tests/images'
# folder containing images already compressed (for comp. test)
templateImagesFolderPath = 'tests/images/templateCompressedImages'
inputImageFilePath = 'tests/images/1.JPG'  # 1st test image
# path of the 1st output image after compression
outputImageFilePath = 'tests/images/.compressed4web/1.JPG'
# template of already compressed image (for comp. test)
templateImageFilePath = 'tests/images/templateCompressedImages/1.JPG'
# images already compressed in the template folder are compressed at 10, if you change test will ko
compressionQuality = 10
numberOfTestImages = 8  # number of images inside the input folder


class compressTenTemplateImages(unittest.TestCase):
    def setUp(self):
        # Setup that runs before each test method
        files.deleteAllFilesInFolder(outputImagesFolderPath)

    def tearDown(self):
        # Clean up that runs after each test method
        files.deleteAllFilesInFolder(outputImagesFolderPath)

    def test_compress_an_image(self):
        compress.compressImage(
            inputImageFilePath, outputImageFilePath, compressionQuality=10)
        self.assertTrue(filecmp.cmp(
            outputImageFilePath, templateImageFilePath))

    def test_compress_all_images_in_folder(self):
        Sync1 = Syncronize(inputImagesFolderPath,
                           outputImagesFolderPath, compressionQuality=10)
        self.assertTrue(len(os.listdir(outputImagesFolderPath))
                        >= numberOfTestImages)
        for i in range(1, 9):
            outputImagePath = os.path.join(
                outputImagesFolderPath, (str(i) + '.JPG'))
            templateImagePath = os.path.join(
                templateImagesFolderPath, (str(i) + '.JPG'))
            self.assertTrue(filecmp.cmp(outputImagePath, templateImagePath))

    def test_resize_an_image(self):
        newWidth = 800  # Example width to resize to
        Sync2 = Syncronize(
            inputImagesFolderPath, outputImagesFolderPath, newWidth=newWidth, mode='resize')
        resizedImagePath = os.path.join(
            outputImagesFolderPath, os.path.basename(inputImageFilePath))
        self.assertTrue(os.path.exists(resizedImagePath))


if __name__ == '__main__':
    unittest.main()
