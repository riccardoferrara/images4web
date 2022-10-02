from os import path, getcwd
from images4web.syncronize import Syncronize
from files import files

# delete images if eventyally present in the compressed folder
files.deleteAllFilesInFolder('src/images4web/images/.compressed4web')
# set input and output path
inputImagePath = path.join(getcwd(), 'src/images4web/images')
outputImagePath = path.join(inputImagePath, '.compressed4web')
# test sync
Sync1 = Syncronize(inputImagePath, outputImagePath, compressionQuality=10)