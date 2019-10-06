
from cvxopt import solvers, matrix
import numpy as np
from food import Food
from post import getPantry
from infoVectors import getUnbounded
from infoVectors import getNutrNames

GLOBAL_DEBUG = False

# here I use linear programming to construct a diet that satisfies many
# nutritional
# requirements and minimizes the amount of calories consumed
# the result is not actually usable in practice
# but we have learned that broccoli is well favored by linear programs


foods_list_global = [
                     'grapefruit',
                     'orange',
                     'bananas',
                     'apples',
                     'tomato',
                     'strawberry',
                     'blackberry',
                     'blueberry',
                     'lemonade',
                     'lemon',
                     'lime',
                     'applesauce',
                     'bread',
                     'noodles',

                     'eggs',
                     'bacon',
                     'sausage',
                     'fish',
                     'chicken',
                     'steak',
                     'beef',
                     'sardine',
                     'beef liver',
                     'liver',
                     'salmon',

                     'milk',
                     'almond milk',
                     'cheese',
                     'yogurt',

                     'broccoli',
                     'spinach',
                     'mushrooms',
                     'carrots',
                     'kale',
                     'cabbage',
                     'eggplant',
                     'onion',
                     'kale',
                     'okra',
                     'rubarb',
                     'potato',

                     'beet',
                     'yam',
                     'white potato',
                     'soybean',
                     'avocado',
                     'sweet potato',
                     'edamame',


                     'lentils',
                     'flax seed',
                     'chia seed',
                     'peanuts',
                     'sunflower seed',
                     'almond',
                     'tofu',
                     'navy bean',
                     'sesame'
                     ]


def main():
    solvers.options['maxiters'] = 300
    # import post
    a = foods_list_global
    pantry = getPantry(a)
    import infoVectors
    # from infoVectors import getVectors
    names, id, lowbound, upbound = infoVectors.getVectors()
    m = len(id)
    n = len(pantry)

    # print 'm'
    # print m
    # print 'n'
    # print n

    A = np.zeros((m, n))
    # print A.shape
    for j in range(n):
        f = np.zeros((m, 1))
        food = pantry[j]
        for i in range(m):
            currId = id[i]
            f[i] = food.get(currId)

        # print 'A, A[:, j], f'
        # print A.shape
        # print A[:, j:j+1].shape
        # print f.shape

        A[:, j:j+1] = f
        # print food.getName()
        # for i in range(m):
        #     print names[i], ": ", f[i]
        # print ''

    # print A

    # create a nutrient matrix using the info vectors
    # m nutrients, n foods

    # m = 31
    N = np.zeros((m*2, n+1))  # needs to be m*2
    for i in range(m):
        nutrientRow = A[i:i+1, :]
        # print 'Ainormation'
        # print A.shape
        # print nutrientRow.shape
        lowerBoundRow = -1*np.c_[nutrientRow, lowbound[i]]
        upperBoundRow = np.c_[nutrientRow, upbound[i]]
        # print lowerBoundRow
        # print upperBoundRow
        N[2*i, :] = lowerBoundRow
        N[2*i+1, :] = upperBoundRow  # 2 * i + 1
        # N[i, :] = upperBoundRow

    # print 'N'
    # print N
    non_negative_food = -1*np.eye(n)
    non_negative_values = np.zeros((n, 1))
    A = N[:, 0:n]
    b = N[:, n:n+1]
    c = np.ones((n, 1)) * -1
    for j in range(14):
        c[j, 0] = 100
    print(b)
    A = np.r_[A, non_negative_food]
    b = np.r_[b, non_negative_values]
    if GLOBAL_DEBUG:
        print(b)
        print(c)
        print(A)
        print(A.shape)
        print(np.linalg.matrix_rank(A))

    # converting to cvxopt compatible data
    As = matrix(A)
    Bs = matrix(b)
    Cs = matrix(c)

    # solve
    sol = solvers.lp(Cs, As, Bs)
    x = np.matrix(sol['x'])

    # print solution and calorie count
    num_foods, one = x.shape
    for i in range(num_foods):
        if x[i] < 10**-4:
            continue
        print('food:', a[i], 'value:', x[i])
    # m, n = A.shape
    # c = np.ones((n, 1))
    # for i in range(m):
    #     x = A[i:i+1, :]
    #     print 'x', x.shape
    #     print 'c', c.shape
    #     print np.dot(x, c)
    # output = np.matrix(x)
    # for i in range()


main()
