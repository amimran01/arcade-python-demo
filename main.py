import os
import sys
from requests import get

"""
Test code
"""
name = os.environ['PYTHON_VAR_username']
ip = get('https://api.ipify.org').text
for x in range(10):
  print(f'Stdout : Hello {name}, your public IP is: {ip}')
  sys.stderr.write(f'Stderr : Hello {name}, your public IP is: {ip}\n')
