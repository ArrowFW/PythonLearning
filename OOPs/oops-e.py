class Circle(object):
    """docstring for Circle."""

    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius
    def set_radius(self, new_radius):
        if isinstance(new_radius, float) and new_radius>0:
            self._radius = new_radius
        else:
            print("Enter the valid value")


my_circle = Circle(5.0)
print(my_circle.get_radius())
my_circle.set_radius(10.0)
print(my_circle.get_radius())
