import numpy
import gdcm

reader = gdcm.ImageReader(
    "D:\#Medicina\#Radiodiagnostica\[#] Archivio Referti\[=] PACS\OPT 2019-2022\A2.orb.1a2b.it.orbassano.S2.891984.1_00000.DCM")
reader.SetFileName(
    "D:\#Medicina\#Radiodiagnostica\[#] Archivio Referti\[=] PACS\OPT 2019-2022\A2.orb.1a2b.it.orbassano.S2.891984.1_00000.DCM")
ret = reader.Read()
if not ret:
    print("It was not possible to read your DICOM file")

print(ret)

image = gdcm.Image()
