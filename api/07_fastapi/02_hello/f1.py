import requests

r = requests.get('http://127.0.0.1:8000/')
print(r.content)
print(r.status_code)