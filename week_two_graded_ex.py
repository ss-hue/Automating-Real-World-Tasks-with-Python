#!/usr/bin/env python3

import os
import requests


path = '/data/feedback/'

docs = os.listdir(path)

dct = {}

def parse_files():

  for d in docs:

    try:
      with open(path + d, 'r', encoding='utf8') as file:
              
        text = file.readlines()

        dct['title'] = text[0].rstrip('\n')
        dct['name'] = text[1].rstrip('\n')
        dct['date'] = text[2].rstrip('\n')
        dct['feedback'] = ''.join(text[3:]).rstrip()

        response = requests.post('http://<corpweb-external-IP>/feedback/', json=dct)
        print(response.status_code) 
    except:
      print('There was an error while opening the file!')

  file.close()  

 
parse_files()
