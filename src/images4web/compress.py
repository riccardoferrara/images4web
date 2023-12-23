from PIL import Image


def compressImage(imagePath, outputImagePath, compressionQuality):
    Im = Image.open(imagePath)
    Im.save(outputImagePath, optimize=True, quality=compressionQuality)


def resizeImage(imagePath, outputImagePath, newWidth):
    Im = Image.open(imagePath)
    width, height = Im.size
    newHeight = int((float(height)/float(width))*float(newWidth))
    Im = Im.resize((newWidth, newHeight), Image.Resampling.LANCZOS)
    Im.save(outputImagePath)
