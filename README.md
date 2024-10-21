# Create Unit Tests Using GitHub Copilot Tools:

The code in

scheduler.py

schedules projects to assignees based on project priority and deadlines. Here's a step-by-step explanation:

1. **Imports**:

   - [`heapq`]: For managing a priority queue.
   - [`datetime`]: For handling project deadlines.

2. **Data Initialization**:

   - [`projects`]: A list of dictionaries, each representing a project with an [`id`], [`priority`], [`name`], and [`deadline`]
   - [`assignees`]: A list of dictionaries, each representing an assignee with an [`id`] and [`name`].

3. **Function [`schedule_projects`]**:

   - **Parameters**: Takes two lists, [`projects`] and [`assignees`].
   - **Sorting Projects**: Projects are sorted by priority (descending) and deadline (ascending).
   - **Assignee Heap**: Initializes a min-heap where each element is a tuple containing the workload (initially 0), assignee name, and assignee dictionary.
   - **Assignment Loop**: Iterates over the sorted projects, assigns each project to the assignee with the least workload, updates the workload, and pushes the updated assignee back into the heap.
   - **Return**: Returns a list of assignments, each containing a project and its assigned assignee.

4. **Main Execution**:
   - Calls `schedule_projects` with the predefined `projects` and `assignees`.
   - Prints the assignments in a readable format.

The output will display each project with its priority, assigned assignee, and deadline.

Example output:

```
Project Alpha (Priority: 5) Assigned To Alice - Deadline: 2022-12-31 23:59:00
Project Epsilon (Priority: 4) Assigned To Bob - Deadline: 2022-12-20 23:59:00
Project Gamma (Priority: 3) Assigned To Charlie - Deadline: 2022-12-15 23:59:00
Project Beta (Priority: 2) Assigned To Alice - Deadline: 2022-11-30 23:59:00
Project Delta (Priority: 1) Assigned To Bob - Deadline: 2022-12-10 23:59:00
```
