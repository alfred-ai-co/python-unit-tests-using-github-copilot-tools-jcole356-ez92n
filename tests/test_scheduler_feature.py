import pytest
from datetime import datetime
from scheduler_feature import schedule_projects

def test_no_projects():
    projects = []
    assignees = [{"id": 1, "name": "Alice"}]
    assignments = schedule_projects(projects, assignees)
    assert assignments == []

def test_no_assignees():
    projects = [{"id": 1, "priority": 5, "name": "Project Alpha", "deadline": datetime(2023, 12, 31, 23, 59)}]
    assignees = []
    assignments = schedule_projects(projects, assignees)
    assert assignments == [{"project": projects[0], "assignees": []}]

def test_single_project_single_assignee():
    projects = [{"id": 1, "priority": 5, "name": "Project Alpha", "deadline": datetime(2023, 12, 31, 23, 59)}]
    assignees = [{"id": 1, "name": "Alice"}]
    assignments = schedule_projects(projects, assignees)
    assert assignments == [{"project": projects[0], "assignees": [assignees[0]]}]

def test_multiple_projects_same_priority_deadline():
    projects = [
        {"id": 1, "priority": 5, "name": "Project Alpha", "deadline": datetime(2023, 12, 31, 23, 59)},
        {"id": 2, "priority": 5, "name": "Project Beta", "deadline": datetime(2023, 12, 31, 23, 59)}
    ]
    assignees = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    assignments = schedule_projects(projects, assignees)
    assert len(assignments) == 2
    assert assignments[0]["project"]["priority"] == 5
    assert assignments[1]["project"]["priority"] == 5

def test_more_projects_than_assignees():
    projects = [
        {"id": 1, "priority": 5, "name": "Project Alpha", "deadline": datetime(2023, 12, 31, 23, 59)},
        {"id": 2, "priority": 4, "name": "Project Beta", "deadline": datetime(2023, 11, 30, 23, 59)}
    ]
    assignees = [{"id": 1, "name": "Alice"}]
    assignments = schedule_projects(projects, assignees)
    assert len(assignments) == 2
    assert len(assignments[0]["assignees"]) == 1
    assert len(assignments[1]["assignees"]) == 1

def test_more_assignees_than_projects():
    projects = [{"id": 1, "priority": 5, "name": "Project Alpha", "deadline": datetime(2023, 12, 31, 23, 59)}]
    assignees = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"},
        {"id": 4, "name": "Diana"}
    ]
    assignments = schedule_projects(projects, assignees)
    assert len(assignments) == 1
    assert len(assignments[0]["assignees"]) == 1

def test_null_projects():
    assignees = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"},
    ]
    with pytest.raises(ValueError, match="Projects and assignees cannot be None"):
        schedule_projects(None, assignees)

def test_null_assignees():
    projects = [
        {"id": 1, "priority": 5, "name": "Project Alpha", "deadline": datetime(2022, 12, 31, 23, 59)},
        {"id": 2, "priority": 2, "name": "Project Beta", "deadline": datetime(2022, 11, 30, 23, 59)},
    ]
    with pytest.raises(ValueError, match="Projects and assignees cannot be None"):
        schedule_projects(projects, None)
