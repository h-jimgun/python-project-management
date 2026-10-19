from models.person import Person
from utils.storage import load_data, save_data

class Project:
    """Represents a project."""
    _id_counter = 1 

    def __init__(self, title, description, due_date):
        self.id = Project._id_counter
        Project._id_counter += 1
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []

    def to_dict(self):
        return {
            "id": self.id, "title": self.title, "description": self.description,
            "due_date": self.due_date, "tasks": self.tasks
        }

class User(Person):
    """Inherits from Person. Represents a system user."""
    def __init__(self, name, email):
        super().__init__(name, email)
        self.projects = []

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email format")
        self._email = value

    def add_project(self, project):
        self.projects.append(project)

    def to_dict(self):
        return {
            "name": self.name, "email": self.email,
            "projects": [p.to_dict() for p in self.projects]
        }