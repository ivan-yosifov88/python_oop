# class Customer:
#     current_id = 0
#
#     def __init__(self, name, address, email):
#         self.name = name
#         self.address = address
#         self.email = email
#         self.id = self.get_next_id()
#
#     def __repr__(self):
#         return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
#
#     @staticmethod
#     def get_next_id():
#         Customer.current_id += 1
#         return Customer.current_id
#
#     @staticmethod
#     def get_next_id():
#         Customer.current_id += 1
#         return Customer.current_id
#

class Customer:
    id = 1

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.id
        Customer.id += 1

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

    @staticmethod
    def get_next_id():
        return Customer.id


