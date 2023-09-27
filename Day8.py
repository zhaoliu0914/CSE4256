import math


class Point:

    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def distance(self, point):
        distance_x = math.pow(self.x - point.x, 2)
        distance_y = math.pow(self.y - point.y, 2)

        return math.sqrt(distance_x + distance_y)


point1 = Point(5, 6)
print(point1)

point2 = Point(3, 1)

distance = point1.distance(point2)
print(distance)