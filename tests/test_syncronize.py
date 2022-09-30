from images4web.classes import syncronize
import os

inputImagePath = os.path.join(os.getcwd(), 'images4web/images')
outputImagePath = os.path.join(inputImagePath, '.compressed4web')
Sync1 = syncronize.Syncronize(inputImagePath, outputImagePath, compressionQuality=10)
