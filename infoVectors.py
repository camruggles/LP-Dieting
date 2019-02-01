# boundingVectors
# copper
# vitamin e


def getVectors():

    unbounded = 100000
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

    id = [208, 204, 606, 601, 307, 306, 205, 291, 203, 269,
          320, 417, 401, 301, 303, 328,
          323, 430, 404, 405, 406, 415,
          418, 410, 421, 312,
          304, 315, 305, 306, 317, 309
          ]

    lowerbounds = [1500, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   900, 400, 90, 900, 8, 15,   # should be 1000 at 4
                   11.7, 120, 1.2, 1.3, 16, 1.3,
                   2.4, 5, 550, 0.9,
                   400, 2.3, 700, 4700, 55, 11
                   ]

    upperbounds = [2500, 65, 20, 300, 2400, 3500, 300, 25, 50, 37.5,
                   3000, 1000, 2000, 2500, 45, 100,
                   990, unbounded, unbounded, unbounded, 35, 100,
                   unbounded, unbounded, 3500, 10,
                   unbounded, 11, 4000, unbounded, 400, 40
                   ]

    return nutrientix, id, lowerbounds, upperbounds
