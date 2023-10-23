import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

url = 'https://x8ee6c4ds4.execute-api.ap-southeast-2.amazonaws.com/test/predict'

data = {'data': [1,1,1,1]}

print(requests.post(url, json=data).json())
