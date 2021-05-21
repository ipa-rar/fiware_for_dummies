import requests

url = "http://localhost:1026/version/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
