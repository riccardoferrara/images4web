from images4web.syncronize import Syncronize
import os

inputImagePath = os.path.join(os.getcwd(), 'tests/images')
outputImagePath = os.path.join(inputImagePath, '.compressed4web')
Sync1 = Syncronize(inputImagePath, outputImagePath, compressionQuality=10)
