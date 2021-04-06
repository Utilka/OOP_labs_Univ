class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GeometricShape:

    def __init__(self):
        pass


class Rectangle(GeometricShape):

    def __init__(self, point_a, point_b, point_c):
        super().__init__()
        self.point_c = point_c
        self.point_b = point_b
        self.point_a = point_a


class Circle(GeometricShape):

    def __init__(self, radius, point_center):
        super().__init__()
        self.radius = radius
        self.point_center = point_center


class Triangle(GeometricShape):

    def __init__(self, point_a, point_b, point_c):
        super().__init__()
        self.point_c = point_c
        self.point_b = point_b
        self.point_a = point_a


class Shape_List:

    def __init__(self):
        pass


if __name__ == '__main__':
    pass
