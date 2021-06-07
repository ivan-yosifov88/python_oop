from project_wild_farm.animals.animal import Mammal
from project_wild_farm.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    PEACE_OF_FOOD = 0.1

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if not isinstance(food, Vegetable) and not isinstance(food, Fruit):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        # self.weight += self.amount_of_increase_weight(food.quantity)
        # self.food_eaten += food.quantity
        self.increase_weight(self.amount_of_increase_weight(food.quantity))
        self.increase_food_eaten(food.quantity)


class Dog(Mammal):
    PEACE_OF_FOOD = 0.4

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        # self.weight += self.amount_of_increase_weight(food.quantity)
        # self.food_eaten += food.quantity
        self.increase_weight(self.amount_of_increase_weight(food.quantity))
        self.increase_food_eaten(food.quantity)


class Cat(Mammal):
    PEACE_OF_FOOD = 0.3

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if not isinstance(food, Vegetable) and not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        # self.weight += self.amount_of_increase_weight(food.quantity)
        # self.food_eaten += food.quantity
        self.increase_weight(self.amount_of_increase_weight(food.quantity))
        self.increase_food_eaten(food.quantity)


class Tiger(Mammal):
    PEACE_OF_FOOD = 1

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        # self.weight += self.amount_of_increase_weight(food.quantity)
        # self.food_eaten += food.quantity
        self.increase_weight(self.amount_of_increase_weight(food.quantity))
        self.increase_food_eaten(food.quantity)
