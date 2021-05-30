class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user):
        if user not in self.user_records:
            return f"We could not find such user to remove!"
        self.user_records.remove(user)
        if user.books:
            user.books.remove(user)


    def change_username(self, user_id, new_username):
        current_user = [user for user in self.user_records if user.user_id == user_id]
        if not current_user:
            return f"There is no user with id = {user_id}!"
        current_user = current_user[0]
        if current_user.username == new_username:
            return "Please check again the provided username - it should be different than the username used so far!"
        current_user.username = new_username
        if current_user.username in self.rented_books:
            current_user.username = new_username
        return f"Username successfully changed to: {new_username} for userid: {user_id}"




