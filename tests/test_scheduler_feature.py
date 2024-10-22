import pytest
from datetime import datetime
from scripts.scheduler_feature import schedule_projects

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

def test_empty_projects_and_assignees():
    """
    Test when both projects and assignees lists are empty.
    """
    with pytest.raises(ValueError):
        schedule_projects([], [])

def test_single_project_no_assignees():
    """
    Test when there is a single project but no assignees.
    """
    projects = [{"id": 1, "priority": 5, "name": "Project Alpha", "deadline": datetime(2022, 12, 31, 23, 59)}]
    with pytest.raises(ValueError):
        schedule_projects(projects, [])

def test_single_assignee_multiple_projects():
    """
    Test when there is a single assignee and multiple projects.
    """
    projects = [
        {"id": 1, "priority": 5, "name": "Project Alpha", "deadline": datetime(2022, 12, 31, 23, 59)},
        {"id": 2, "priority": 4, "name": "Project Beta", "deadline": datetime(2022, 12, 30, 23, 59)},
    ]
    assignees = [{"id": 1, "name": "Alice"}]
    assignments = schedule_projects(projects, assignees)
    assert len(assignments) == 2
    assert assignments[0]["assignees"][0]["name"] == "Alice"
    assert assignments[1]["assignees"][0]["name"] == "Alice"

def test_projects_with_same_priority_different_deadlines(assignees):
    """
    Test when projects have the same priority but different deadlines.
    """
    projects = [
        {"id": 1, "priority": 5, "name": "Project Alpha", "deadline": datetime(2022, 12, 31, 23, 59)},
        {"id": 2, "priority": 5, "name": "Project Beta", "deadline": datetime(2022, 12, 30, 23, 59)},
    ]
    assignments = schedule_projects(projects, assignees)
    assert len(assignments) == 2
    assert assignments[0]["project"]["name"] == "Project Alpha"
    assert assignments[1]["project"]["name"] == "Project Beta"

def test_projects_with_different_priorities_same_deadline(assignees):
    """
    Test when projects have different priorities but the same deadline.
    """
    projects = [
        {"id": 1, "priority": 5, "name": "Project Alpha", "deadline": datetime(2022, 12, 31, 23, 59)},
        {"id": 2, "priority": 4, "name": "Project Beta", "deadline": datetime(2022, 12, 31, 23, 59)},
    ]
    assignments = schedule_projects(projects, assignees)
    assert len(assignments) == 2
    assert assignments[0]["project"]["priority"] == 5
    assert assignments[1]["project"]["priority"] == 4

def test_projects_with_same_priority_and_deadline(assignees):
    """
    Test when projects have the same priority and the same deadline.
    """
    projects = [
        {"id": 1, "priority": 5, "name": "Project Alpha", "deadline": datetime(2022, 12, 31, 23, 59)},
        {"id": 2, "priority": 5, "name": "Project Beta", "deadline": datetime(2022, 12, 31, 23, 59)},
    ]
    assignments = schedule_projects(projects, assignees)
    assert len(assignments) == 2
    assert assignments[0]["project"]["name"] in ["Project Alpha", "Project Beta"]
    assert assignments[1]["project"]["name"] in ["Project Alpha", "Project Beta"]

def test_assignees_with_no_projects():
    """
    Test when there are assignees but no projects.
    """
    assignees = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
    ]
    assignments = schedule_projects([], assignees)
    assert assignments == []

def test_projects_with_no_deadline(assignees):
    """
    Test when projects have no deadlines.
    """
    projects = [
        {"id": 1, "priority": 5, "name": "Project Alpha", "deadline": None},
        {"id": 2, "priority": 4, "name": "Project Beta", "deadline": None},
    ]
    assignments = schedule_projects(projects, assignees)
    assert len(assignments) == 2
    assert assignments[0]["project"]["name"] == "Project Alpha"
    assert assignments[1]["project"]["name"] == "Project Beta"

def test_no_projects(assignees):
    """
    Test when there are no projects.
    """
    assignments = schedule_projects([], assignees)
    assert assignments == []

def test_no_assignees(projects):
    """
    Test when there are no assignees.
    """
    with pytest.raises(ValueError):
        schedule_projects(projects, [])

def test_single_project_single_assignee():
    """
    Test when there is a single project and a single assignee.
    """
    projects = [{"id": 1, "priority": 5, "name": "Project Alpha", "deadline": datetime(2022, 12, 31, 23, 59)}]
    assignees = [{"id": 1, "name": "Alice"}]
    assignments = schedule_projects(projects, assignees)
    assert len(assignments) == 1
    assert assignments[0]["project"]["name"] == "Project Alpha"
    assert assignments[0]["assignees"][0]["name"] == "Alice"

def test_multiple_projects_same_priority_deadline(assignees):
    """
    Test when multiple projects have the same priority and deadline.
    """
    projects = [
        {"id": 1, "priority": 5, "name": "Project Alpha", "deadline": datetime(2022, 12, 31, 23, 59)},
        {"id": 2, "priority": 5, "name": "Project Beta", "deadline": datetime(2022, 12, 31, 23, 59)},
    ]
    assignments = schedule_projects(projects, assignees)
    assert len(assignments) == 2
    assert assignments[0]["project"]["priority"] == 5
    assert assignments[1]["project"]["priority"] == 5

def test_more_projects_than_assignees(assignees):
    """
    Test when there are more projects than assignees.
    """
    projects = [
        {"id": 1, "priority": 5, "name": "Project Alpha", "deadline": datetime(2022, 12, 31, 23, 59)},
        {"id": 2, "priority": 4, "name": "Project Beta", "deadline": datetime(2022, 12, 30, 23, 59)},
        {"id": 3, "priority": 3, "name": "Project Gamma", "deadline": datetime(2022, 12, 29, 23, 59)},
        {"id": 4, "priority": 2, "name": "Project Delta", "deadline": datetime(2022, 12, 28, 23, 59)},
    ]
    assignments = schedule_projects(projects, assignees)
    assert len(assignments) == 4
    assert assignments[0]["assignees"][0]["name"] == "Alice"
    assert assignments[1]["assignees"][0]["name"] == "Bob"
    assert assignments[2]["assignees"][0]["name"] == "Charlie"
    assert assignments[3]["assignees"][0]["name"] == "Alice"  # Alice gets another project

def test_more_assignees_than_projects(projects):
    """
    Test when there are more assignees than projects.
    """
    assignees = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"},
        {"id": 4, "name": "David"},
    ]
    assignments = schedule_projects(projects, assignees)
    assert len(assignments) == 5
    assigned_assignees = [assignment["assignees"][0]["name"] for assignment in assignments]
    assert "Alice" in assigned_assignees
    assert "Bob" in assigned_assignees
    assert "Charlie" in assigned_assignees
    assert "David" in assigned_assignees

if __name__ == "__main__":
    pytest.main()
