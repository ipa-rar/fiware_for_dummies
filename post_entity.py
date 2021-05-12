import requests
import json

url = "http://localhost:1026/v2/entities/"

payload = json.dumps({
  "type": "Store",
  "id": "urn:ngsi-ld:Store:002",
  "address": {
    "type": "PostalAddress",
    "value": {
      "streetAddress": "Friedrichstraße 44",
      "addressRegion": "Berlin",
      "addressLocality": "Kreuzberg",
      "postalCode": "10969"
    },
    "metadata": {
      "verified": {
        "value": True,
        "type": "Boolean"
      }
    }
  },
  "location": {
    "type": "geo:json",
    "value": {
      "type": "Point",
      "coordinates": [
        13.3903,
        52.5075
      ]
    }
  },
  "name": {
    "type": "Text",
    "value": "Checkpoint Markt"
  }
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
