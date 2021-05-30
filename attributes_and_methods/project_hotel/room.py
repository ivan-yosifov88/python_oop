class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    @staticmethod
    def can_take_room(capacity, people, is_taken):
        return not is_taken and people <= capacity

    @staticmethod
    def can_free_room(is_taken):
        return is_taken

    def take_room(self, people):
        if not self.can_take_room(self.capacity, people, self.is_taken):
            return f"Room number {self.number} cannot be taken"
        self.is_taken = True
        self.guests = people

    def free_room(self):
        if not self.can_free_room(self.is_taken):
            return f"Room number {self.number} is not taken"
        self.is_taken = False
        self.guests = 0
