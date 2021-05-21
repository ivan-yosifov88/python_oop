from todo_list.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        filter_task = [t for t in self.tasks if new_task == t]
        if filter_task:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        filter_task = [t for t in self.tasks if t.name == task_name]
        if not filter_task:
            return f"Could not find task with the name {task_name}"
        filter_task[0].completed= True
        return f"Completed task {task_name}"

    def clean_section(self):
        amount_of_removed_tasks = 0
        for t in self.tasks:
            if t.completed:
                self.tasks.remove(t)
                amount_of_removed_tasks += 1
        return f"Cleared {amount_of_removed_tasks} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"
        for t in self.tasks:
            result += f"{t.details()}\n"
        return result


