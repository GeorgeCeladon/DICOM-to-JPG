import pydicom as dicom
import os
import cv2
import PIL
from pydicom.pixel_data_handlers.util import apply_voi_lut
from pydicom.pixel_data_handlers.util import apply_windowing
import matplotlib.pyplot as plt
import numpy as np


# make it True if you want in PNG format
PNG = False

# Specify the .dcm folder path
folder_path = "D:\#Medicina\#Radiodiagnostica\[#] Archivio Referti\[=] PACS\OPT 2019-2022"

# Specify the output jpg/png folder path
jpg_folder_path = "D:\#Medicina\#Radiodiagnostica\[#] Archivio Referti\[=] PACS\OPT 2019-2022\OPT JPG"

# Per ogni file contenuto nella cartella
images_path = os.listdir(folder_path)
for n, image in enumerate(images_path):
    ds = dicom.dcmread(os.path.join(folder_path, image))


# Se serve eseguire un controllo stampa i parametri del dicom
#    print('DICOM PRE-MODIFICA')
#    print(ds)

# Definisci i valori di finestra (centro e apertura) da utilizzare (senza salvarli nel file)
#    ds.WindowCenter = "4447"
#    ds.WindowWidth = "3589"

# Produci l'immagine usando i parametri del DICOM e quelli modificati
    pixel_array_numpy = ds.pixel_array

#    pixel_array_numpy_2 = apply_voi_lut(
#        pixel_array_numpy, ds, index=0, prefer_lut=True)

    img = pixel_array_numpy
#    window_center = ds.WindowCenter
#    window_width = ds.WindowWidth

#    scaled_img = cv2.convertScaleAbs(
#        img-window_center, alpha=(255.0 / window_width))

    scaled_img = cv2.convertScaleAbs(
        img-np.min(img), alpha=(255 / min(np.max(img)-np.min(img), 8000,)))


#    pixel_array_numpy_3 = apply_windowing(
#        pixel_array_numpy, ds)

# Se serve eseguire un controllo stampa i parametri del dicom
#    print('DICOM POST-MODIFICA')
#     print(ds)

# Definisci il formato di esportazione ed esporta
    if PNG == False:
        image = image.replace('.DCM', '.jpg')
    else:
        image = image.replace('.DCM', '.png')

    id_studio = ds.AccessionNumber
    image_rename = id_studio + " " + image
#    print(image)
#    print(image_rename)

    cv2.imwrite(os.path.join(jpg_folder_path, image_rename), scaled_img)

# Stampa il numero di dicom convertiti ogni 5 conversioni
    if n % 5 == 0:
        print('{} image converted'.format(n))
