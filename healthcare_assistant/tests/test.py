import requests

url = 'http://localhost:8000/ask'

question = "Is Ankara Medical Centre operational on weekends?" 

data = {"question": question}

response = requests.post(url, json=data)

print(response.json())
