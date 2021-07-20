from requests import get
import os

name = os.environ['PYTHON_VAR_username']
ip = get('https://api.ipify.org').text
print(f'Hello {name}, your public IP is: {ip}')
