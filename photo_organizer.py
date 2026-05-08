import os
from os import listdir

#
folder_dir = r"C:\Users\mi16747\Photos"
for images in os.listdir(folder_dir):

    if (images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg")):
        print(images)

