class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.animals_in_zoo = 0
        self.__workers_capacity = workers_capacity
        self.workers_in_zoo = 0
        self.name = name
        self.animals = []
        self.workers = []

    @staticmethod
    def get_worker(worker_name, workers):
        ll = [worker for worker in workers if worker.name == worker_name]
        if ll:
            return ll[0]

    @staticmethod
    def is_enough_space(objects_count, avalilable_space):
        return objects_count < avalilable_space

    @staticmethod
    def is_budget_enough(money_spent, budget):
        return money_spent <= budget

    @staticmethod
    def get_sum_animals_costs(animals):
        costs = 0
        for animal in animals:
            costs += animal.get_needs()

        return costs

    @staticmethod
    def get_sum_workers_costs(workers):
        costs = 0
        for worker in workers:
            costs += worker.salary
        return costs

    @staticmethod
    def filter_list_with_class_name(obj_list, class_name):
        result = [obj for obj in obj_list if obj.__class__.__name__ == class_name]
        return result

    def add_animal(self, animal, price):
        if not self.is_enough_space(self.animals_in_zoo, self.__animal_capacity):
            return f"Not enough space for animal"

        if not price < self.__budget:
            return f"Not enough budget"

        self.animals.append(animal)
        self.animals_in_zoo += 1
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if not self.is_enough_space(self.workers_in_zoo, self.__workers_capacity):
            return "Not enough space for worker"

        self.workers.append(worker)
        self.workers_in_zoo += 1
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        current_worker = self.get_worker(worker_name, self.workers)
        if not current_worker:
            return f"There is no {worker_name} in the zoo"
        self.workers_in_zoo -= 1
        self.workers.remove(current_worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        needed_money_for_salaries = self.get_sum_workers_costs(self.workers)
        if not self.is_budget_enough(needed_money_for_salaries, self.__budget):
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= needed_money_for_salaries
        left_budget = self.__budget
        return f"You payed your workers. They are happy. Budget left: {left_budget}"

    def tend_animals(self):
        needed_money_to_tend_animals = self.get_sum_animals_costs(self.animals)
        if not self.is_budget_enough(needed_money_to_tend_animals, self.__budget):
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= needed_money_to_tend_animals
        left_budget = self.__budget
        return f"You tended all the animals. They are happy. Budget left: {left_budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        total_animals_count = len(self.animals)
        lions = self.filter_list_with_class_name(self.animals, "Lion")
        tigers = self.filter_list_with_class_name(self.animals, "Tiger")
        cheetahs = self.filter_list_with_class_name(self.animals, "Cheetah")
        animals_list = [lions, tigers, cheetahs]
        result = f"You have {total_animals_count} animals"
        for animals in animals_list:
            result += '\n'f"----- {len(animals)} {animals[0].__class__.__name__}s:"+"\n" + '\n'.join([f"{a}" for a in animals])
        # result += f"----- {len(lions)} Lions""\n"
        # result += '\n'.join([f"{lion}" for lion in lions]) + "\n"
        # result += f"----- {len(tigers)} Tigers""\n"
        # result += '\n'.join([f"{tiger}" for tiger in tigers]) + "\n"
        # result += f"----- {len(cheetahs)} Cheetahs""\n"
        # result += '\n'.join([f"{cheetah}" for cheetah in cheetahs])

        return result

    def workers_status(self):
        total_workers_count = len(self.workers)
        keeper = self.filter_list_with_class_name(self.workers, "Keeper")
        caretaker = self.filter_list_with_class_name(self.workers, "Caretaker")
        vet = self.filter_list_with_class_name(self.workers, "Vet")
        workers_list = [keeper, caretaker, vet]
        result = f"You have {total_workers_count} workers"
        for workers in workers_list:
            result += '\n'f"----- {len(workers)} {workers[0].__class__.__name__}s:"+"\n" + '\n'.join([f"{w}" for w in workers])

        return result


