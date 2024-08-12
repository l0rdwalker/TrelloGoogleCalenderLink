import requests
import json

url = "https://api.trello.com/1/cards/6368f2af63728b03c6a0b6a6"

headers = {
   "Accept": "application/json"
}

query = {
   'key': '82fe777c0c901c458eeb2f019a0ead31',
   'token': '8643256dc3060028cae72c4bcd1c24841ad667db3f9d3077f20ea444e6cdf795',
   'name':'Sicko',
   'due':'2022-11-08T02:22:00.000Z',
   'start':'2022-11-06T21:00:41.866Z'
}

response = requests.request(
   "PUT",
   url,
   headers=headers,
   params=query
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))