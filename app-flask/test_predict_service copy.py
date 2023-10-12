import requests

url = 'http://0.0.0.0:6969/predict'

data = {'data': [1,2,3,4]}

print(requests.post(url, json=data).json())
