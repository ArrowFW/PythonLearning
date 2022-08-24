#getters and Setters
class Backpack:
    """docstring for Getters and Setters method ."""

    def __init__(self):
        self._items = []



    def get_items(self):
        return self._items

    def set_items(self, new_items):
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print("Please Enter Valid String")

new_backpack = Backpack()
print(new_backpack.get_items())
new_backpack.set_items(['pen','Pencil','Eracer'])
print(new_backpack.get_items())
