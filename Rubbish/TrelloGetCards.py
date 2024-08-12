import requests

url = "https://api.trello.com/1/boards/yC7Zhtvy/cards"

query = {
   'key': '82fe777c0c901c458eeb2f019a0ead31',
   'token': '8643256dc3060028cae72c4bcd1c24841ad667db3f9d3077f20ea444e6cdf795'
}

response = requests.request(
   "GET",
   url,
   params=query
)

print(response.text)