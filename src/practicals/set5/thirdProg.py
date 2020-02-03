class gridPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x, self.y + other.y

    def __str__(self):
        string = string + "," + str(self.y)
        return string


point1 = gridPoint(3, 5)
point2 = gridPoint(-1, 4)
point3 = point1 + point2

print(point3)