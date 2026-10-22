import pytest
from models.user import User, Project
from models.task import Task

def test_user_email_validation():
    with pytest.raises(ValueError):
        User("Alex", "not-an-email")
        
    with pytest.raises(ValueError):
        User("Star", "star_at_gmail.com")
    
    user1 = User("Alex", "alex@example.com")
    user2 = User("Star", "star@gmail.com")
    
    assert user1.email == "alex@example.com"
    assert user2.email == "star@gmail.com"

def test_task_defaults():
    task = Task("Write code")
    assert task.status == "Pending"
    assert task.assigned_to == "Unassigned"

def test_task_completion():
    task = Task("Write code")
    task.complete()
    assert task.status == "Complete"

def test_project_creation():
    project = Project("CLI Tool", "Build a CLI", "2026-12-01")
    assert project.title == "CLI Tool"
    assert len(project.tasks) == 0
    
    task = Task("Fix bug")
    project.tasks.append(task.to_dict())
    assert len(project.tasks) == 1