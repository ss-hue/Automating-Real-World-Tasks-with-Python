#!/usr/bin/env python3

import requests
import os, sys
import glob
import subprocess

pwd = subprocess.Popen('pwd', stdout=subprocess.PIPE, universal_newlines=True).stdout.read().strip()


#Completes the path selecting the actual directory where all the image files are located.
path_imgs = pwd + '/supplier-data/images/'



#Returns a list containing a list of all the entries in the directory given by path.
dirs = os.listdir(path_imgs)

url = 'http://<IP Address>/upload/'


for d in dirs:
 
  if d.endswith('.jpeg'):

    try:
      with open(path_imgs + d, 'rb') as opened:
                
        r = requests.post(url, files={'file': opened})

    except:

      print('Something went wrong: The file(s) coudln`t be uploaded')
