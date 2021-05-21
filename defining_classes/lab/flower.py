class Flower:

    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity):
        if self.water_requirements <= quantity:
            self.is_happy = True

    def status(self):
        if not self.is_happy:
            return f"{self.name} is not happy"
        return f"{self.name} is happy"


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(100)
print(flower.status())
