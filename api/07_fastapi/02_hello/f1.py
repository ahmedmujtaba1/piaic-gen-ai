import requests

r = requests.post('http://127.0.0.1:8000/hi_post')
print(r.content)
print(r.status_code)