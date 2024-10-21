import pytest
from datetime import datetime
from scripts.scheduler import schedule_projects

@pytest.fixture
def projects():
    return [
        {"id": 1, "priority": 5, "name": "Project Alpha", "deadline": datetime(2022, 12, 31, 23, 59)},
        {"id": 2, "priority": 2, "name": "Project Beta", "deadline": datetime(2022, 11, 30, 23, 59)},
        {"id": 3, "priority": 3, "name": "Project Gamma", "deadline": datetime(2022, 12, 15, 23, 59)},
        {"id": 4, "priority": 1, "name": "Project Delta", "deadline": datetime(2022, 12, 10, 23, 59)},
        {"id": 5, "priority": 4, "name": "Project Epsilon", "deadline": datetime(2022, 12, 20, 23, 59)},
    ]

@pytest.fixture
def assignees():
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"},
    ]

def test_no_projects(assignees):
    assignments = schedule_projects([], assignees)
    assert assignments == []

def test_no_assignees(projects):
    with pytest.raises(ValueError):
        schedule_projects(projects, [])

def test_single_project_single_assignee():
    projects = [{"id": 1, "priority": 5, "name": "Project Alpha", "deadline": datetime(2022, 12, 31, 23, 59)}]
    assignees = [{"id": 1, "name": "Alice"}]
    assignments = schedule_projects(projects, assignees)
    assert len(assignments) == 1
    assert assignments[0]["project"]["name"] == "Project Alpha"
    assert assignments[0]["assignee"]["name"] == "Alice"

def test_multiple_projects_same_priority_deadline(assignees):
    projects = [
        {"id": 1, "priority": 5, "name": "Project Alpha", "deadline": datetime(2022, 12, 31, 23, 59)},
        {"id": 2, "priority": 5, "name": "Project Beta", "deadline": datetime(2022, 12, 31, 23, 59)},
    ]
    assignments = schedule_projects(projects, assignees)
    assert len(assignments) == 2
    assert assignments[0]["project"]["priority"] == 5
    assert assignments[1]["project"]["priority"] == 5

def test_more_projects_than_assignees(assignees):
    projects = [
        {"id": 1, "priority": 5, "name": "Project Alpha", "deadline": datetime(2022, 12, 31, 23, 59)},
        {"id": 2, "priority": 4, "name": "Project Beta", "deadline": datetime(2022, 12, 30, 23, 59)},
        {"id": 3, "priority": 3, "name": "Project Gamma", "deadline": datetime(2022, 12, 29, 23, 59)},
        {"id": 4, "priority": 2, "name": "Project Delta", "deadline": datetime(2022, 12, 28, 23, 59)},
    ]
    assignments = schedule_projects(projects, assignees)
    assert len(assignments) == 4
    assert assignments[0]["assignee"]["name"] == "Alice"
    assert assignments[1]["assignee"]["name"] == "Bob"
    assert assignments[2]["assignee"]["name"] == "Charlie"
    assert assignments[3]["assignee"]["name"] == "Alice"  # Alice gets another project

def test_more_assignees_than_projects(projects):
    assignees = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"},
        {"id": 4, "name": "David"},
    ]
    assignments = schedule_projects(projects, assignees)
    assert len(assignments) == 5
    assigned_assignees = [assignment["assignee"]["name"] for assignment in assignments]
    assert "Alice" in assigned_assignees
    assert "Bob" in assigned_assignees
    assert "Charlie" in assigned_assignees
    assert "David" in assigned_assignees

if __name__ == "__main__":
    pytest.main()
