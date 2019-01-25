import requests
# import json

url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'

headers = {
    'Content-Type': 'application/json',
    'x-app-id': 'no',
    'x-app-key': 'no'
}

# body = [("query", "for breakfast i ate 2 eggs, bacon, and french toast")]
body = "{\"query\": \"eggs\"}"
r = requests.post(url, headers=headers, data=body)

print r.json()
