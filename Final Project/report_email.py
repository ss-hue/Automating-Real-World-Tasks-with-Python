#!/usr/bin/env python3

import os
import datetime
import reports
import emails
import subprocess

pwd = subprocess.Popen('pwd', stdout=subprocess.PIPE, universal_newlines=True).stdout.read().strip()

path = pwd + '/supplier-data/descriptions/'


docs = os.listdir(path)

rpt = []

def rpt_email():
    
  for d  in docs:
      
    try:
      with open(path + d, 'r', encoding='utf8') as file:
              
        text = file.readlines()

        rpt.append('name: {}<br/>weight: {}\n'.format(text[0].rstrip('\n'), text[1].rstrip('\n')))
 
    except:
      print('There was an error while opening the file!')
    
  return rpt



if __name__ == "__main__":

  attachment = '/tmp/processed.pdf'

  title = 'Processed Updated on {}'.format(datetime.date.today())
    
  paragraph = '<br\>'.join(rpt_email())
    
  reports.generate_report(attachment, title, paragraph)

  subject = "Upload Completed - Online Fruit Store"

  sender = "automation@example.com"

  receiver = "{}@example.com".format(os.environ.get('USER'))

  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

  message = emails.generate_email(sender, receiver, subject, body, attachment)
    
  emails.send_email(message)