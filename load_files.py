import pydicom
from pydicom.data import get_testdata_file
import matplotlib.pyplot as plt

# get sample file path automatically
file_path = get_testdata_file("CT_small.dcm")

ds = pydicom.dcmread(file_path)

image = ds.pixel_array

plt.imshow(image, cmap='gray')
plt.title("Sample DICOM")
plt.axis('off')
plt.show()