from asyncore import write
import pydicom as dicom
import os
import cv2
import PIL
from pydicom.pixel_data_handlers.util import apply_voi_lut
from pydicom.pixel_data_handlers.util import apply_windowing
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import re

# Specify the .dcm folder path
folder_path = "D:\#Medicina\#Radiodiagnostica\[#] Archivio Referti\[=] PACS\OPT 2019-2022"

blank = ""

with open("rs-output.csv", "w") as f:
    f.write(blank)

# Per ogni file contenuto nella cartella
images_path = os.listdir(folder_path)
for n, image in enumerate(images_path):
    ds = dicom.dcmread(os.path.join(folder_path, image))
    ds_str = str(ds)

    ds_str_rgx_0 = re.sub(",", " ", ds_str)
    ds_str_rgx_1 = re.sub("^", "'", ds_str_rgx_0)
    ds_str_rgx_2 = re.sub("\n", "','", ds_str_rgx_1)
    ds_str_rgx_3 = re.sub("$", "'\n", ds_str_rgx_2)

    with open("rs-output.csv", "a") as f:
        f.write(ds_str_rgx_3)
