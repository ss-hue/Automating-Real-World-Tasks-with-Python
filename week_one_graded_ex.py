#!/usr/bin/env python3

import os, sys
import subprocess
from PIL import Image

#Gets the actual path where the program is located.
pwd = subprocess.Popen('pwd', stdout=subprocess.PIPE, universal_newlines=True).stdout.read().strip()

#Completes the path selecting the actual directory where all the image files are located.
path_imgs = pwd + '/images/'

#Returns a list containing a list of all the entries in the directory given by path.
dirs = os.listdir(path_imgs)

#This will be the directory where the updated image files will be located.
output_path ='/opt/icons/'


#Iterates through all the files in the directory and uses Image object in order to modify and update them.
def new_file():

  for dr in dirs:
    try:
      with Image.open(path_imgs + dr) as img:
      
        img.resize((128,128)).rotate(-90).convert('RGB').save(output_path + dr, 'JPEG')

    except:
      pass


#Shows the updated image files formats and sizes.
def show_format_size():

  for dr in dirs:
    try:
      with Image.open(output_path + dr) as img:

        print(img.format, img.size)

    except:
      pass


new_file()
show_format_size()