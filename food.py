
class Food:

    def __init__(self, name, nutrientdict):
        self.foodName = name
        self.n = nutrientdict

    def toString(self):
        print self.foodName
        print self.n

    def get(self, i):
        return self.n.get(i, 0)

    def getName(self):
        return self.foodName

    def getN(self):
        return self.n
