
import requests
from infoVectors import getVectors
from food import Food
import sys


def main():
    if len(sys.argv) < 2:
        print 'You need to input a food in the command line'
        quit()
    url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'

    headers = {
        'Content-Type': 'application/json',
        'x-app-id': '7962ef8a',
        'x-app-key': '2a3fdd11d1f548aaf05164ee920a5ae3'
    }

    body = "{\"query\": \""
    body += sys.argv[1] + ', '
    body += '\"}'

    r = requests.post(url, headers=headers, data=body)
    data = r.json()

    foods = data['foods']
    food = foods[0]

    # foodName = food['food_name']  # getting the food name
    fullNutrients = food['full_nutrients']  # getting information

    n = {}  # dictionary containing all the nutrients and their values
    for nutrient in fullNutrients:
        nutrientid = nutrient['attr_id']
        nutrientValue = nutrient['value']
        n[nutrientid] = nutrientValue  # uploading nutr info to dict

    # f = Food(foodName, n)

    nutrientix, id, lowerbounds, upperbounds = getVectors()
    d = {}
    for i in range(len(id)):
        d[id[i]] = nutrientix[i]

    print d
    # keychain = f.getN()
    for k in n.keys():
        if d.get(k, None) is None:
            continue
        print k, ':', d.get(k), ': ', n.get(k, 0)


main()
