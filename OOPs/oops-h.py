class Backpack:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

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


my_backpack = Backpack()
# print(my_backpack.items)
my_backpack.add_item('pencil')
# print(my_backpack.items)
my_backpack.add_item('paper')
# print(my_backpack.items)
# my_backpack.remove_item('pencil')
# my_backpack.remove_item('pencil')
# print(my_backpack.items)
has_pencil = my_backpack.has_item("pencil")
print(has_pencil)
