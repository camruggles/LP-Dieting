'''
POST https://trackapi.nutritionix.com/v2/natural/nutrients
Content-Type:application/json,
x-app-id:7962ef8a,
x-app-key:2a3fdd11d1f548aaf05164ee920a5ae3
{
 "query":"for breakfast i ate 2 eggs, bacon, and french toast",
 "timezone": "US/Eastern"
}
'''
import requests
# import json

url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'

headers = {
    'Content-Type': 'application/json',
    'x-app-id': '7962ef8a',
    'x-app-key': '2a3fdd11d1f548aaf05164ee920a5ae3'
}

# body = [("query", "for breakfast i ate 2 eggs, bacon, and french toast")]
body = "{\"query\": \"eggs\"}"
r = requests.post(url, headers=headers, data=body)

print r.json()
