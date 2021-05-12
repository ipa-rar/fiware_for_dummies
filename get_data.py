import requests

url = "http://localhost:1026/v2/entities"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
