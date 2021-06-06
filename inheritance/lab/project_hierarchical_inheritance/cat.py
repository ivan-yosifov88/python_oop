from project_hierarchical_inheritance.animal import Animal


class Cat(Animal):
    @staticmethod
    def meow():
        return "meowing..."