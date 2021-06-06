from project_multiple_inheritance.employee import Employee
from project_multiple_inheritance.person import Person


class Teacher(Person, Employee):
    @staticmethod
    def teach():
        return "teaching..."