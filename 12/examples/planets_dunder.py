class Planet():
    def __init__(self, name_in, radius_in, mass_in):
        self.name = name_in
        self.radius = radius_in
        self.mass = mass_in

    def getData(self):
        return {"name": self.name, "radius": self.radius, "mass": self.mass}

    def changeName(self, newname):
        self.name = newname

    def __ge__(self, other):
        if self.radius >= other.radius and self.mass >= other.mass:
            return True
        return False

    def __lt__(self, other):
        return False if self.__ge__(other) else True

    def __str__(self):
        return f"----------------------------------------\nName: \t{self.name}\nRadius:\t{self.radius} km\nMass: \t{self.mass} kg\n----------------------------------------"

earth = Planet("Earth", 6371, 5.972e24)
mars = Planet("Mars", 3389, 6.39e23)
print(earth >= mars)
print(mars < earth)
print(earth < mars)
print(earth)
