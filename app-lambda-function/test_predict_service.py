import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

data = {'data': '1,2,3,4'}

print(requests.post(url, json=data).json())
