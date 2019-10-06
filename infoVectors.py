# boundingVectors
# copper
# vitamin e

unbounded = 100000
unbound = 100000


def getUnbounded():
    return unbounded


def getNutrNames():

    nutrientix = ['calories',
                  'fat',
                  'saturated fatty acids',
                  'cholesterol',
                  'sodium',
                  'potassium',
                  'carbs',
                  'fiber',
                  'protein',
                  'sugar',

                  'vitamin a',
                  'folate',
                  'vitamin c',
                  'calcium',
                  'iron',
                  'vitamin d',

                  'vitamim e',
                  'vitamin k',
                  'thiamin',
                  'riboflavin',
                  'niacin',
                  'vitamin b6',

                  'vitamin b12',
                  'pantothenic acid',
                  'choline',
                  'copper',

                  'magnesium',
                  'manganese',
                  'phosphorus',
                  'potassium',
                  'selenium',
                  'zinc'
                  ]
    return nutrientix


def getVectors():

    nutrientix = ['calories',
                  'fat',
                  'saturated fatty acids',
                  'cholesterol',
                  'sodium',
                  'potassium',
                  'carbs',
                  'fiber',
                  'protein',
                  'sugar',

                  'vitamin a',
                  'folate',
                  'vitamin c',
                  'calcium',
                  'iron',
                  'vitamin d',

                  'vitamim e',
                  'vitamin k',
                  'thiamin',
                  'riboflavin',
                  'niacin',
                  'vitamin b6',

                  'vitamin b12',
                  'pantothenic acid',
                  'choline',
                  'copper',

                  'magnesium',
                  'manganese',
                  'phosphorus',
                  'selenium',
                  'zinc'
                  ]

    id = [208, 204, 606, 601, 307, 306, 205, 291, 203, 269,
          320, 417, 401, 301, 303, 328,
          323, 430, 404, 405, 406, 415,
          418, 410, 421, 312,
          304, 315, 305, 317, 309
          ]

    lowerbounds = [1800, 0, 0, 0, 0, 4700, 0, 25, 50, 0,  # 6 should be
                   # 4700 potassium
                   900, 400, 90, 1000, 8, 15,   # should be 15 at 6 vitamin d
                   11.7, 120, 1.2, 1.3, 16, 1.3,
                   2.4, 5, 550, 0.9,  # 3 should be 550 choline
                   400, 2.3, 700, 55, 11
                   ]

    # sugar should be at 37.5 and carbs at 300 :
    upperbounds = [2200, 65, 20, 300, 2400, unbound, 300, unbound, 100, 15,
                   3000, 1000, 2000, 2500, 45, 100,
                   990, unbounded, unbounded, unbounded, 35, 100,
                   unbounded, unbounded, 3500, 10,
                   unbounded, 11, 4000, 400, 40
                   ]

    return nutrientix, id, lowerbounds, upperbounds
