class Dog:

    species = "Canis Lupus"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

print(Dog.species)
c=Dog('Tigher', 12, 'hi-breed')
print(c.name)
