from project_pizza_calories.dough import Dough
from project_pizza_calories.topping import Topping


class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.__name = name
        self.__dough = dough
        self.__toppings_capacity = toppings_capacity
        self.__toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        self.__toppings_capacity = value

    @property
    def toppings(self):
        return self.__toppings

    @toppings.setter
    def toppings(self, value):
        self.__toppings = value

    @staticmethod
    def is_space_for_topping(toppings_dict, capacity):
        def get_topping_count(toppings_dict):
            if not toppings_dict:
                return 0
            return len([topping for topping in toppings_dict])

        topping_count = get_topping_count(toppings_dict)
        return topping_count < capacity

    def add_topping(self, topping):
        if not self.is_space_for_topping(self.toppings, self.toppings_capacity):
            raise ValueError("Not enough space for another topping")
        if topping.topping_type not in self.toppings:
            self.toppings[topping.topping_type] = 0
        self.toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self):
        return sum(self.toppings.values()) + self.dough.weight


