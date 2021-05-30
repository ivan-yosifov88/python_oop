class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    def __repr__(self):
        # result = ""
        # result += '\n'.join([f"{customer}"for customer in self.customers])
        # result += "\n"
        # result += '\n'.join([f"{dvd}" for dvd in self.dvds])
        #
        # return result
        return '\n'.join([f"{customer}"for customer in self.customers]) + '\n' + '\n'.join([f"{dvd}" for dvd in self.dvds])

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    @staticmethod
    def is_customer(customer_id, customers):
        ll = [customer for customer in customers if customer.customer_id == customer_id]
        if ll:
            return ll[0]

    @staticmethod
    def is_dvd(dvd_id, rented_dvds):
        ll = [dvd for dvd in rented_dvds if dvd_id == dvd.customer_id]
        if ll:
            return ll[0]

    @staticmethod
    def is_age_valid(customer_age, age_restriction):
        return customer_age < age_restriction

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.is_customer(customer_id, self.customers)
        dvd = self.is_dvd(dvd_id, self.dvds)
        if self.is_age_valid(customer.age, dvd.age_restriction):
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        if dvd.is_rented and not dvd in customer.rented_dvds:
            return "DVD is already rented"
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.is_customer(customer_id, self.customers)
        dvd = self.is_dvd(dvd_id, customer.rented_dvds)
        if not dvd:
            return f"{customer.name} does not have that DVD"
        dvd.is_rented = False
        customer.rented_dvds.remove(dvd)
        return f"{customer.name} has successfully returned {dvd.name}"
