from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def animal_sound(self):
        pass


class Cat(Animal):
    def animal_sound(self):
        print('meow')


class Dog(Animal):
    def animal_sound(self):
        print('woof-woof')


class Chicken(Animal):
    def animal_sound(self):
        print("chick-chick")


cat = Cat()
dog = Dog()
chicken = Chicken()

animals = [cat, dog]
for animal in animals:
    animal.animal_sound()
animals.append(chicken)
for animal in animals:
    animal.animal_sound()


