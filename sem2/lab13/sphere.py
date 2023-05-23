import math


class Sphere:

    def __init__(self, radius=None, x=None, y=None, z=None):
        self.radius = 1.0 if radius is None else radius
        self.x = 0.0 if x is None else x
        self.y = 0.0 if y is None else y
        self.z = 0.0 if z is None else z

    def get_volume(self):
        return 4 / 3 * math.pi * pow(self.radius, 3)

    def get_square(self):
        return 4 * math.pi * pow(self.radius, 2)

    def is_point_inside(self, x, y, z):
        deltaX = pow((self.x - x), 2)
        deltaY = pow((self.y - y), 2)
        deltaZ = pow((self.z - z), 2)
        return (deltaX + deltaY + deltaZ) < pow(self.radius, 2)

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.x, self.y, self.z

    def set_radius(self, r):
        self.radius = r

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


s0 = Sphere(0.5)  # test sphere creation with radius and default center
print(s0.get_center())  # (0.0, 0.0, 0.0)
print(s0.get_volume())  # 0.523598775598
print(s0.is_point_inside(0, -1.5, 0))  # False
s0.set_radius(1.6)
print(s0.is_point_inside(0, -1.5, 0))  # True
print(s0.get_radius())  # 1.6
