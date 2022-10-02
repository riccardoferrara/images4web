from PIL import Image

def compressImage(imagePath, outputImagePath, compressionQuality):
    Im = Image.open(imagePath)
    Im.save(outputImagePath, optimize=True, quality=compressionQuality) 