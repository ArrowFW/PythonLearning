class Circle(object):
    """docstring for Circle."""
    CON_COLOR = ('RED', 'YELLOW', 'BLUE')

    def __init__(self, radius, color):
        self._radius = radius
        self._color = color

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, int) and new_radius > 0:
            self._radius = new_radius
        else:
            print("Please Enter a Valid value property.")
    radius = property(get_radius, set_radius)

    def get_color(self):
        return self._color

    def set_color(self, new_color):
        if new_color in Circle.CON_COLOR:
            self._color = new_color
        else:
            print("Enter a Valid Color")

    color = property(get_color, set_color)


my_circle = Circle(10, "RED")
print(my_circle.radius)
print(my_circle.color)
