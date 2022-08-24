class Backpack:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def add_multi_item(self, items):
        for item in items:
            self.add_item(item)

    def add_item(self, new_item):
        if isinstance(new_item, str):
            self._items.append(new_item)
        else:
            print("Provide a Valid Name: ")

    def remove_item(self, new_item):
        if new_item in self._items:
            self._items.remove(new_item)
            return 1
        else:
            return 0

    def has_item(self, item):
        return item in self._items

    def show_item(self, sorted_item=False):
        if sorted_item:
            print(sorted(self._items))
        else:
            print(self._items)


my_backpack = Backpack()
my_backpack.add_multi_item(["Pen", "Pencil", "Ink", "Eraser"])
print(my_backpack.items)
my_backpack.add_item("Paper")
print(my_backpack.items)
