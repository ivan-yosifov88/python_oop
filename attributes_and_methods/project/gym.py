class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    # @staticmethod
    # def is_element_in_list(element, list_of_elements):
    #     return element in list_of_elements
    #
    # def add_customer(self, customer):
    #     if not self.is_element_in_list(customer, self.customers):
    #         self.customers.append(customer)
    #
    # def add_trainer(self, trainer):
    #     if not self.is_element_in_list(trainer, self.trainers):
    #         self.trainers.append(trainer)
    #
    # def add_equipment(self, equipment):
    #     if not self.is_element_in_list(equipment, self.equipments):
    #         self.equipments.append(equipment)
    #
    # def add_plan(self, plan):
    #     if not self.is_element_in_list(plan, self.plans):
    #         self.plans.append(plan)
    #
    # def add_subscription(self, subscription):
    #     if not self.is_element_in_list(subscription, self.subscriptions):
    #         self.subscriptions.append(subscription)


    @staticmethod
    def is_element_not_in_list_then_append(element, list_of_elements):
        def append_in_list(element, list_of_elements):
            list_of_elements.append(element)
        if element not in list_of_elements:
            append_in_list(element, list_of_elements)

    @staticmethod
    def get_id(id, list_of_id):
        result = [element for element in list_of_id if element.id == id]
        if result:
            return result[0]


    def add_customer(self, customer):
        self.is_element_not_in_list_then_append(customer, self.customers)

    def add_trainer(self, trainer):
        self.is_element_not_in_list_then_append(trainer, self.trainers)

    def add_equipment(self, equipment):
        self.is_element_not_in_list_then_append(equipment, self.equipment)

    def add_plan(self, plan):
        self.is_element_not_in_list_then_append(plan, self.plans)

    def add_subscription(self, subscription):
        self.is_element_not_in_list_then_append(subscription, self.subscriptions)

    def subscription_info(self, subscription_id):
        subscription = self.get_id(subscription_id, self.subscriptions)
        if subscription:
            customer = self.get_id(subscription.customer_id, self.customers)
            trainer = self.get_id(subscription.trainer_id, self.trainers)
            plan = self.get_id(subscription.exercise_id, self.plans)
            equipment = self.get_id(plan.equipment_id, self.equipment)

            return f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{plan}"
