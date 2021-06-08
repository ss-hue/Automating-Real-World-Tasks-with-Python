#!/usr/bin/env python3

import re
import os, sys
import subprocess
from PIL import Image

#Gets the actual path where the program is located.
pwd = subprocess.Popen('pwd', stdout=subprocess.PIPE, universal_newlines=True).stdout.read().strip()


#Completes the path selecting the actual directory where all the image files are located.
path_imgs = pwd + '/supplier-data/images/'

#Returns a list containing a list of all the entries in the directory given by path.
dirs = os.listdir(path_imgs)

#This will be the directory where the updated image files will be located.
output_path = pwd + '/supplier-data/images/'


#Iterates through all the files in the directory and uses Image object in order to modify and update them.
def new_file():

  for dr in dirs:
    if '.tiff' in dr:
      try:
        with Image.open(path_imgs + dr) as img:
          img.resize((600,400)).convert('RGB').save(output_path + dr, 'JPEG')
          
      except:
        pass
    os.rename(output_path + dr, re.sub('(?=\.).*', '.jpeg', output_path + dr))


new_file()