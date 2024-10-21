import heapq
from datetime import datetime

# List of projects with their details
projects = [
    {"id": 1, "priority": 5, "name": "Project Alpha", "deadline": datetime(2022, 12, 31, 23, 59)},
    {"id": 2, "priority": 2, "name": "Project Beta", "deadline": datetime(2022, 11, 30, 23, 59)},
    {"id": 3, "priority": 3, "name": "Project Gamma", "deadline": datetime(2022, 12, 15, 23, 59)},
    {"id": 4, "priority": 1, "name": "Project Delta", "deadline": datetime(2022, 12, 10, 23, 59)},
    {"id": 5, "priority": 4, "name": "Project Epsilon", "deadline": datetime(2022, 12, 20, 23, 59)},
]

# List of assignees with their details
assignees = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"},
]

def schedule_projects(projects, assignees):
    # Sort projects by priority (descending) and deadline (ascending)
    projects.sort(key=lambda x: (x["priority"], x["deadline"]), reverse=True)

    # Initialize a min-heap for assignees with their current workload (initially 0)
    assignee_heap = [(0, assignee["name"], assignee) for assignee in assignees]
    heapq.heapify(assignee_heap)

    assignments = []

    # Assign each project to the assignee with the least workload
    for project in projects:
        # Pop the assignee with the least workload from the heap
        workload, assignee_name, assignee = heapq.heappop(assignee_heap)

        # Assign the project to this assignee
        assignments.append({"project": project, "assignee": assignee})

        # Increment the workload of the assignee
        workload += 1

        # Push the updated assignee back into the heap
        heapq.heappush(assignee_heap, (workload, assignee_name, assignee))

    return assignments

if __name__ == "__main__":
    # Schedule the projects and print the assignments
    assignments = schedule_projects(projects, assignees)
    for assignment in assignments:
        project = assignment["project"]
        assignee = assignment["assignee"]
        print(f"{project['name']} (Priority: {project['priority']}) Assigned To {assignee['name']} - Deadline: {project['deadline']}")
