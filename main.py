import os
import sys
import time
from requests import get

"""
Test code
"""
name = os.environ['PYTHON_VAR_username']
ip = get('https://api.ipify.org').text
for x in range(10):
  time.sleep(0.2)
  print(f'Stdout : Hello {name}, your public IP is: {ip}')
  time.sleep(0.2)
  sys.stderr.write(f'Stderr : Hello {name}, your public IP is: {ip}\n')
