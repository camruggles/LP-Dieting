
from cvxopt import solvers, matrix
import numpy as np
from food import Food

# here I use linear programming to construct a diet that satisfies many
# nutritional
# requirements and minimizes the amount of calories consumed
# the result is not actually usable in practice
# but we have learned that broccoli is well favored by linear programs


def LP():

    # label = ['calories', 'iron', 'protein', 'calcium',
    #         'vitamin A', 'vitamin C',
    #         'fat', 'sodium']
    rice = [210, 2, 5, 0, 0, 0, 3.5, 150]
    milk = [30, 4, 1, 45, 10, 0, 2.5, 170]
    bananas = [89.9, 1, 1.1, 1, 1, 15, 0.3, 1]
    broccoli = [30.9, 4, 2.6, 4, 11, 135, 0.3, 30]
    beans = [120, 10, 8, 4, 0, 0, 0, 85]

    # constructing A and c
    A = np.matrix([rice, milk, bananas, broccoli, beans])
    A = A.T
    c = np.matrix(A[0, :])
    A = A[1:, :]

    # constructing b
    b = np.matrix([100, 61.2, 100, 100, 100, 77, 2300])
    b = b.reshape(7, 1)

    # converting inequality constraints to Ax <= b
    X = np.c_[A, b]
    X[0:5, :] *= -1

    # enforcing non negative solution vector
    nonzeros = -1*np.eye(5, 5)
    z = np.zeros(5)
    Z = np.c_[nonzeros, z]
    X = np.r_[X, Z]

    # separating A and b
    m, n = X.shape
    b = X[:, n-1]
    A = X[:, :n-1]

    # converting to cvxopt compatible data
    As = matrix(A)
    Bs = matrix(b)
    Cs = matrix(c.T)

    # solve
    sol = solvers.lp(Cs, As, Bs)
    x = np.matrix(sol['x'])

    # print solution and calorie count
    print x
    print c*x


def main():
    # import post
    from post import getPantry
    a = ['eggs', 'bacon', 'milk', 'sausage', 'broccoli']
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
        print food.getName()
        for i in range(m):
            print names[i], ": ", f[i]
        print ''

    print A


main()
