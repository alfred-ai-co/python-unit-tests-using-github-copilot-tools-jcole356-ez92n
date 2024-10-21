import pytest
from datetime import datetime
from scheduler import schedule_projects

@pytest.fixture
def projects():
    return [
        {"id": 1, "priority": 5, "name": "Project Alpha", "deadline": datetime(2023, 12, 31, 23, 59)},
        {"id": 2, "priority": 2, "name": "Project Beta", "deadline": datetime(2023, 11, 30, 23, 59)},
        {"id": 3, "priority": 3, "name": "Project Gamma", "deadline": datetime(2023, 12, 15, 23, 59)},
        {"id": 4, "priority": 1, "name": "Project Delta", "deadline": datetime(2023, 12, 10, 23, 59)},
        {"id": 5, "priority": 4, "name": "Project Epsilon", "deadline": datetime(2023, 12, 20, 23, 59)},
    ]

@pytest.fixture
def assignees():
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"},
        {"id": 4, "name": "Diana"},
        {"id": 5, "name": "Evan"},
    ]

def test_schedule_projects_collaborative_assignment(projects, assignees):
    assignments=schedule_projects(projects, assignees)
    for assignment in assignments:
        assert len(assignment["assignees"])>1, f"{assignment['project']['name']} is not assigned collaboratively!"