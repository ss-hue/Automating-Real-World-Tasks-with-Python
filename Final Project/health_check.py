#!/usr/bin/env python3

from emails import generate_error_report, send_email
import socket
import os
import psutil
import shutil
import time


s_time = time.time()


def cpu_usage():

  return psutil.cpu_percent(60)

def disk_space():

  d_usage = shutil.disk_usage("/")

  return round((d_usage.free/d_usage.total)*100, 2)

def vr_memory():

  return psutil.virtual_memory().available/(1024*1024)

def check_host():

  return socket.gethostname('localhost')


def alert(alert):
    
  sender = "automation@example.com"

  receiver = "{}@example.com".format(os.environ.get('USER'))

  subject = "Error - {}".format(alert)

  body = "Please check your system and resolve the issue as soon as possible"

  message = generate_error_report(sender, receiver, subject, body)
    
  send_email(message)


while True:

  if cpu_usage() > 80:
        
    alert('CPU usage is over 80%')
    
  if disk_space() < 20:

    alert('Available disk space is less than 20%')

  if vr_memory() < 500:

    alert('Available memory is less than 500MB')

  if check_host() != '127.0.0.1':

    alert('localhost cannot be resolved to 127.0.0.1')



  time.sleep(60 - time() % 60)


