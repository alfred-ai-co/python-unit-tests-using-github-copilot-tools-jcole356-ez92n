import heapq
from datetime import datetime

projects=[
    {"id": 1, "priority": 5, "name": "Project Alpha", "deadline": datetime(2022, 12, 31, 23, 59)},
    {"id": 2, "priority": 2, "name": "Project Beta", "deadline": datetime(2022, 11, 30, 23, 59)},
    {"id": 3, "priority": 3, "name": "Project Gamma", "deadline": datetime(2022, 12, 15, 23, 59)},
    {"id": 4, "priority": 1, "name": "Project Delta", "deadline": datetime(2022, 12, 10, 23, 59)},
    {"id": 5, "priority": 4, "name": "Project Epsilon", "deadline": datetime(2022, 12, 20, 23, 59)},
]

assignees=[
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"},
]

def schedule_projects(projects, assignees):
    projects.sort(key=lambda x: (x["priority"], x["deadline"]), reverse=True)
    assignee_heap = [(0, assignee["name"], assignee) for assignee in assignees]
    heapq.heapify(assignee_heap)
    assignments = []
    for project in projects:
        project_assignees = []
        assignees_per_project=(len(assignees)+1)//4
        for _ in range(assignees_per_project):
            if assignee_heap:
                workload, assignee_name, assignee=heapq.heappop(assignee_heap)
                project_assignees.append(assignee)
                workload+=1
                heapq.heappush(assignee_heap, (workload, assignee_name, assignee))
        assignments.append({"project": project, "assignees": project_assignees})
    return assignments

if __name__=="__main__":
    assignments=schedule_projects(projects, assignees)
    for assignment in assignments:
        project=assignment["project"]
        assignees=assignment["assignees"]
        assignee_names=", ".join(assignee['name'] for assignee in assignees)
        print(f"{project['name']} (Priority: {project['priority']}) Assigned To {assignee_names} - Deadline: {project['deadline']}")