import requests


url = "http://127.0.0.1:5000/register"


params = {"username": "observ", "password": "password", "question": "chr", "question_content": "只因你太美"}
# params = {"username": "observer", "password": "password"}

resp = requests.post(url, params=params)
print(resp.json())