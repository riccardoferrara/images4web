from os import path, remove, getcwd
from . import folder
from . import settings
from . import compress


class Syncronize:
    def __init__(self, inputFolderPath, outputFolderPath, compressionQuality='', newWidth=None, mode='compress'):
        self.compressionQuality = compressionQuality if compressionQuality else settings.compressionQuality
        self.newWidth = newWidth if newWidth else settings.newWidth
        self.mode = mode  # 'compress' or 'resize'
        self.InputFolder = folder.InputFolder(inputFolderPath)
        self.OutputFolder = folder.OutputFolder(outputFolderPath)
        self.what2sync()
        self.syncCompressOrResize()
        self.syncDelete()

    def syncCompressOrResize(self):
        if not self.loi2sync:
            return
        print('\nProcess images from folder %s:' % self.InputFolder.path)
        for image_name in self.loi2sync:
            input_image_path = path.join(self.InputFolder.path, image_name)
            output_image_path = path.join(self.OutputFolder.path, image_name)

            if self.mode == 'compress':
                compress.compressImage(
                    input_image_path, output_image_path, self.compressionQuality)
                action = 'compressed'
            elif self.mode == 'resize':
                compress.resizeImage(
                    input_image_path, output_image_path, self.newWidth)
                action = 'resized'
            else:
                print('Invalid mode specified.')
                continue
            print('%s %s' % (image_name, action))

    def syncDelete(self):
        if not self.loi2del:
            return
        print('\nDelete images from folder %s:' % self.OutputFolder.path)
        for image_name in self.loi2sync:
            remove(path.join(self.OutputFolder.path, image_name))

    def what2sync(self):
        self.loi2sync = list(set(self.InputFolder.loi) -
                             set(self.OutputFolder.loi))
        self.loi2del = list(set(self.OutputFolder.loi) -
                            set(self.InputFolder.loi))


def testSynrconize():
    inputImagePath = path.join(getcwd(), 'src/images4web/images')
    outputImagePath = path.join(inputImagePath, '.compressed4web')

    # Example usage for compress mode
    Sync1 = Syncronize(inputImagePath, outputImagePath,
                       compressionQuality=10, mode='compress')

    # Example usage for resize mode
    Sync2 = Syncronize(inputImagePath, outputImagePath,
                       newWidth=800, mode='resize')


if __name__ == '__main__':
    testSynrconize()
