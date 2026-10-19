class Task:
    def __init__(self, title, status="Pending", assigned_to="Unassigned"):
        self.title = title
        self.status = status
        self.assigned_to = assigned_to

    def complete(self):
        self.status = "Complete"

    def to_dict(self):
        return {"title": self.title, "status": self.status, "assigned_to": self.assigned_to}