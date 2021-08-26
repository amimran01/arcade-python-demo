import os
from requests import get

"""
Test code
"""
name = os.environ['PYTHON_VAR_username']
ip = get('https://api.ipify.org').text
for x in range(100):
  print(f'Hello {name}, your public IP is: {ip}')

