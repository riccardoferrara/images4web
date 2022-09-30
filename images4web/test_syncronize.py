from classes.syncronize import *
import os

inputImagePath = os.path.join(os.getcwd(), 'images4web/images')
outputImagePath = os.path.join(inputImagePath, '.compressed4web')
Sync1 = Syncronize(inputImagePath, outputImagePath, compressionQuality=10)
