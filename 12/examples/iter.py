class Animal:
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} is {self.age} old and a {self.type}!"


class Animallist:
    def __init__(self):
        self.animals = []
        self.index = 0

    def __add__(self, animal: Animal):
        if animal not in self.animals:
            self.animals.append(animal)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        while self.index < len(self.animals):
            self.index += 1
            return self.animals[self.index-1].__str__()
        raise StopIteration

joe = Animal("Joe", "Dog", 5)
bob = Animal("Bob", "Cat", 3)
my_animals = Animallist()
my_animals + joe #  add animals to list
my_animals + bob
for animal in my_animals:
    print(animal)

