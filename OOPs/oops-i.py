# Default Method
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self, change=5):
        self.y += change

    def move_down(self, change=5):
        self.y -= change

    def move_right(self, change=5):
        self.x += change

    def move_left(self, change=5):
        self.x -= change


my_player = Player(10, 5)

print("y initialy : ", my_player.y)
print("x initially :", my_player.x)
my_player.move_up()

print("y:", my_player.y)
my_player.move_down()

print("y:", my_player.y)
my_player.move_right()

print("x:", my_player.x)
my_player.move_left()

print("x:", my_player.x)
