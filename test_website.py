import requests

url = 'http://localhost:6969/predict'

data = {'data':1}

print(requests.post(url, json=data).json())