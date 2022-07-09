import pydicom as dicom
import PIL  # optional
import pandas as pd
import matplotlib.pyplot as plt

# specify your image path
image_path = 'D:\#Medicina\#Radiodiagnostica\[#] Archivio Referti\[=] PACS\OPT 2019-2022\A2.orb.5b74.it.orbassano.S1.2782934.1_00000.DCM'
ds = dicom.dcmread(image_path)
plt.imshow(ds.pixel_array, cmap=plt.cm.gray)

plt.show()
print(ds)
