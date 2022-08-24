class Backpack:
    """docstring for Backpack."""

    def __init__(self):
        self._items = []

    @property
    def items(self):
        print("Calling the Getter")
        return self._items

    @items.setter
    def items(self, new_items):
        print("Calling the Setter")
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print("Enter the Valid list of items")


my_backpack = Backpack()
print(my_backpack.items)
my_backpack.items = ["pen", "pencil"]
print(my_backpack.items)
