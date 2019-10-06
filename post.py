
import requests
# declaring class information for storage purposes

from food import Food


def getPantry(foodInput):

    # constructing request for data

    url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'

    headers = {
        'Content-Type': 'application/json',
        'x-app-id': '7962ef8a',
        'x-app-key': '2a3fdd11d1f548aaf05164ee920a5ae3'
    }

    body = "{\"query\": \""
    for str in foodInput:
        body += str + ', '
    body += '\"}'
    # print body
    # body = "{\"query\": \"eggs, bacon, cheese, milk,\"}"
    # print body

    # executing the request

    r = requests.post(url, headers=headers, data=body)
    data = r.json()

    # constructing and returning an array of the foods
    Pantry = []
    foods = data['foods']  # getting all the food from the json
    for food in foods:
        foodName = food['food_name']  # getting the food name
        fullNutrients = food['full_nutrients']  # getting information
        n = {}  # dictionary containing all the nutrients and their values
        for nutrient in fullNutrients:
            nutrientid = nutrient['attr_id']
            nutrientValue = nutrient['value']
            n[nutrientid] = nutrientValue  # uploading nutr info to dict
        Pantry.append(Food(foodName, n))  # constructing food object

    return Pantry
