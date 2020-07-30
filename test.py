import requests

url = "http://127.0.0.1:5000/run"
d = {'code': 'print("Hi")'}
r = requests.post(url, data=d)
print(r.text)
