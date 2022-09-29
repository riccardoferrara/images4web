from syncronize import Syncronize
import os

inputImagePath = '/Users/riccardoperso/Library/CloudStorage/OneDrive-SharedLibraries-GruppoFerrovieDelloStato/DOIT MI - OFI/Visite Generali/02_UT LINEE NORD/P.S.PIETRO-CALOLZIOCORTE/13+119/04_Ispezione Generale'
outputImagePath = os.path.join(inputImagePath, '.compressed4web')
Sync1 = Syncronize(inputImagePath, outputImagePath)