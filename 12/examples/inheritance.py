class Animal():
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age
    
    def make_sound(self):
        print("I am an animal!")

    def __str__(self) -> str:
        return f"{self.name} is {self.age} old and a {self.type}!"

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Cat", age)

    def make_sound(self):
        print("Meow!")

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Dog", age)

    def make_sound(self):
        print("Woof!")

dogo = Dog("Dogo", 5)
cat = Cat("Cat", 3)
dogo.make_sound()  # Woof!
cat.make_sound()  # Meow!

class Frog(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Frog", age)
my_frog = Frog("Frog", 1)
my_frog.make_sound()  # I am an animal!