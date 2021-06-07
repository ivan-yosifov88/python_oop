from project_wild_farm.animals.animal import Bird
from project_wild_farm.food import *


class Owl(Bird):
    PEACE_OF_FOOD = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        # self.weight += self.amount_of_increase_weight(food.quantity)
        # self.food_eaten += food.quantity
        self.increase_weight(self.amount_of_increase_weight(food.quantity))
        self.increase_food_eaten(food.quantity)


class Hen(Bird):
    PEACE_OF_FOOD = 0.35

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        if not isinstance(food, Food):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        # self.weight += self.amount_of_increase_weight(food.quantity)
        # self.food_eaten += food.quantity
        self.increase_weight(self.amount_of_increase_weight(food.quantity))
        self.increase_food_eaten(food.quantity)