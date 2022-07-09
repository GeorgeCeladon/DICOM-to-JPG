import pydicom as dicom
import os
import cv2
import PIL
from pydicom.pixel_data_handlers.util import apply_voi_lut
from pydicom.pixel_data_handlers.util import apply_windowing
import matplotlib.pyplot as plt


# make it True if you want in PNG format
PNG = True

# Specify the .dcm folder path
folder_path = "D:\#Medicina\#Radiodiagnostica\[#] Archivio Referti\[=] PACS\OPT 2019-2022"

# Specify the output jpg/png folder path
jpg_folder_path = "D:\#Medicina\#Radiodiagnostica\[#] Archivio Referti\[=] PACS\OPT 2019-2022\OPT JPG"

images_path = os.listdir(folder_path)
for n, image in enumerate(images_path):
    ds = dicom.dcmread(os.path.join(folder_path, image))

    ds.WindowCenter = "4000"
    ds.WindowWidth = "6000"

    pixel_array_numpy = ds.pixel_array
    pixel_array_numpy_2 = apply_voi_lut(
        pixel_array_numpy, ds, prefer_lut=False)
    pixel_array_numpy_3 = apply_windowing(
        pixel_array_numpy_2, ds
    )
    print(ds)

    if PNG == False:
        image = image.replace('.DCM', '.jpg')
    else:
        image = image.replace('.DCM', '.png')

    cv2.imwrite(os.path.join(jpg_folder_path, image), pixel_array_numpy_3)

    if n % 50 == 0:
        print('{} image converted'.format(n))
