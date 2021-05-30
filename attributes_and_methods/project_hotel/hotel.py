class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        if room not in self.rooms:
            self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number and not room.take_room(people):
                self.guests += people
                break

    def free_room(self, room_number):
        for room in self.rooms:
            room_guests = room.guests
            if room.number == room_number and not room.free_room():
                self.guests -= room_guests
                break

    def print_status(self):
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]
#         print(
#             f'''Hotel {self.name} has {self.guests} total guests
# Free rooms: {", ".join(free_rooms)}
# Taken rooms: {", ".join(taken_rooms)}'''
#         )
        print(f"Hotel {self.name} has {self.guests} total guests")
        if free_rooms:
            print(f"Free rooms: {', '.join(free_rooms)}")
        if taken_rooms:
            print(f"Taken rooms: {', '.join(taken_rooms)}")