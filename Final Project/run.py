#!/usr/bin/env python3

import os
import re
import locale
import requests
import subprocess

locale.setlocale(locale.LC_ALL, '')

pwd = subprocess.Popen('pwd', stdout=subprocess.PIPE, universal_newlines=True).stdout.read().strip()


#Completes the path selecting the actual directory where all the image files are located.
path_dsc = pwd + '/supplier-data/descriptions/'



docs = os.listdir(path_dsc)

dct = {}

def parse_files():

  for d in docs:
    
    try:
      with open(path_dsc + d, 'r', encoding='utf8') as file:
              
        text = file.readlines()
      
        dct['name'] = text[0].rstrip('\n')
        dct['weight'] = int(locale.atof(text[1].rstrip('\n').rstrip(' lbs')))
        dct['description'] = ''.join(text[2:]).rstrip()
        dct['image_name'] = re.sub('(?=\.).*', '.jpeg', d)
      
      response = requests.post('http://<IP address>/fruits/', json=dct)
      print(response.status_code)
 
    except:
      print('There was an error while opening the file!')
    

parse_files()
