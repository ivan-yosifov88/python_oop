class Cup:

    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters):
        if self.quantity + milliliters <= self.size:
            self.quantity += milliliters

    def status(self):
        result = self.size - self.quantity
        return result


cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())
