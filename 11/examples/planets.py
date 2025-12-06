class Planet():
    def __init__(self, name_in, radius_in, mass_in):
        self.name = name_in
        self.radius = radius_in
        self.mass = mass_in

    def getData(self):
        return {"name": self.name, "radius": self.radius, "mass": self.mass}

    def changeName(self, newname):
        self.name = newname

earth = Planet("Earth", 6371, 5.972e24)
mars = Planet("Mars", 3389, 6.39e23)
earth_data = earth.getData()
print(earth_data["name"])  # Earth
earth.changeName("Earth2.0")
earth_data = earth.getData()
print(earth_data["name"])  # Earth2.0
