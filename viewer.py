import pydicom as dicom
import PIL  # optional
import pandas as pd
import matplotlib.pyplot as plt

# specify your image path
image_path = 'D:\#Medicina\#Radiodiagnostica\[#] Archivio Referti\[=] PACS\OPT 2019-2022\A2.orb.1a2b.it.orbassano.S2.891984.1_00000.dcm'
ds = dicom.dcmread(image_path)
plt.imshow(ds.pixel_array, cmap=plt.cm.gray)

plt.show()
print(ds)
