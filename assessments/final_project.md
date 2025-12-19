# Final Project: Task Management System

**Due After Completing Module 10: Sorting Algorithms**  
**Time Estimate:** 8-12 hours over 2-3 weeks  
**Total Points:** 200

---

## Overview

Build a comprehensive **Task Management System** (similar to Trello, Asana, or Todoist) that demonstrates mastery of all data structures and algorithms covered in this course. This capstone project requires you to integrate at least 5 different data structures and multiple algorithms to create a functional, efficient task management application.

## Learning Objectives

By completing this project, you will demonstrate:
- ✅ Proficiency with all major data structures (arrays, linked lists, stacks, queues, hash tables, trees, graphs)
- ✅ Understanding of searching and sorting algorithms
- ✅ Ability to choose appropriate data structures for specific requirements
- ✅ Skills in implementing complex systems with multiple interacting components
- ✅ Experience with real-world software design and optimization

---

## Problem Statement

Create a task management system that helps users organize, prioritize, and track their tasks efficiently. The system should support:
- Creating and managing tasks with various attributes
- Organizing tasks into projects and categories
- Tracking task dependencies (Task B can't start until Task A is done)
- Priority-based task scheduling
- Efficient search and filtering
- Undo/redo functionality
- Task history and analytics

---

## Core Requirements

### Feature 1: Task Management (30 points)

Implement comprehensive task CRUD operations:

#### Task Structure
Each task must have:
- `task_id`: Unique identifier (auto-generated)
- `title`: Task title (string)
- `description`: Detailed description (string)
- `priority`: Priority level (1-5, where 5 is highest)
- `status`: Current status ("todo", "in_progress", "completed", "blocked")
- `due_date`: Due date (datetime or string in format "YYYY-MM-DD")
- `project_id`: Associated project (string/integer)
- `tags`: List of tags for categorization (list of strings)
- `dependencies`: List of task IDs that must be completed first
- `created_at`: Timestamp of creation
- `completed_at`: Timestamp of completion (None if not completed)

#### Required Methods

```python
class TaskManager:
    def create_task(self, title, description, priority, due_date, project_id, tags=None):
        """Create a new task. Returns task_id."""
        pass
    
    def update_task(self, task_id, **kwargs):
        """Update task attributes. Returns True if successful."""
        pass
    
    def delete_task(self, task_id):
        """Delete a task. Returns True if successful."""
        pass
    
    def get_task(self, task_id):
        """Retrieve a task by ID. O(1) time complexity required."""
        pass
    
    def mark_complete(self, task_id):
        """Mark a task as completed with timestamp."""
        pass
```

**Data Structure Requirements:**
- Use **hash table** for O(1) task lookup by ID
- Use **hash table** for O(1) project lookup
- Use **hash table** (with sets/lists as values) for tag-based indexing

---

### Feature 2: Task Dependencies (Graph) (30 points)

Implement task dependencies using graph data structures:

```python
def add_dependency(self, task_id, depends_on_task_id):
    """
    Add a dependency: task_id depends on depends_on_task_id.
    Should detect circular dependencies.
    """
    pass

def remove_dependency(self, task_id, depends_on_task_id):
    """Remove a dependency relationship."""
    pass

def get_dependencies(self, task_id):
    """Get all tasks that this task depends on."""
    pass

def get_dependents(self, task_id):
    """Get all tasks that depend on this task."""
    pass

def can_start_task(self, task_id):
    """Check if a task can be started (all dependencies completed)."""
    pass

def get_task_order(self):
    """
    Return a valid order to complete all tasks (topological sort).
    Returns: List of task IDs in valid completion order
    """
    pass

def detect_circular_dependencies(self):
    """
    Detect if there are any circular dependencies in the task graph.
    Returns: True if circular dependencies exist, False otherwise
    """
    pass
```

**Data Structure Requirements:**
- Use **directed graph** (adjacency list) to represent dependencies
- Implement **topological sort** to determine task order
- Implement **cycle detection** (using DFS) to prevent circular dependencies

---

### Feature 3: Priority Queue for Task Scheduling (25 points)

Implement priority-based task scheduling:

```python
def get_next_task(self):
    """
    Get the highest priority task that can be started now.
    Priority determined by: priority level, due date, dependencies.
    Returns: Task object or None
    """
    pass

def get_top_priority_tasks(self, limit=10):
    """
    Get the top N priority tasks that are ready to start.
    Returns: List of task objects
    """
    pass

def get_overdue_tasks(self):
    """
    Get all tasks past their due date that aren't completed.
    Returns: List of task objects sorted by how overdue they are
    """
    pass

def schedule_tasks(self):
    """
    Generate an optimal task schedule based on priorities and dependencies.
    Returns: Ordered list of tasks to work on
    """
    pass
```

**Data Structure Requirements:**
- Use **priority queue** (heap) for efficient priority-based retrieval
- Combine priority score from multiple factors (priority level + due date proximity)
- Must support O(log n) insertion and O(log n) extraction

---

### Feature 4: Search and Filtering (25 points)

Implement efficient search and filter operations:

```python
def search_tasks_by_title(self, query):
    """
    Search tasks by title (substring match, case-insensitive).
    Returns: List of matching task objects
    """
    pass

def search_tasks_by_tag(self, tag):
    """
    Get all tasks with a specific tag. O(1) average case required.
    Returns: List of task objects
    """
    pass

def filter_tasks(self, project_id=None, status=None, priority=None, 
                 min_priority=None, max_priority=None):
    """
    Filter tasks by multiple criteria.
    Returns: List of matching task objects
    """
    pass

def get_tasks_by_project(self, project_id):
    """
    Get all tasks in a specific project. O(1) average case required.
    Returns: List of task objects
    """
    pass

def get_tasks_due_in_range(self, start_date, end_date):
    """
    Get all tasks due within a date range.
    Returns: List of task objects sorted by due date
    """
    pass
```

**Data Structure Requirements:**
- Use **hash tables** with tag and project indices for O(1) lookups
- Implement efficient filtering with multiple criteria
- Use **binary search** on sorted date ranges when applicable

---

### Feature 5: Sorting and Organization (20 points)

Implement multiple sorting options for tasks:

```python
def sort_tasks_by_priority(self, tasks, ascending=False):
    """
    Sort tasks by priority level.
    Must implement a comparison-based sort (merge sort or quick sort).
    """
    pass

def sort_tasks_by_due_date(self, tasks):
    """Sort tasks by due date (earliest first)."""
    pass

def sort_tasks_by_title(self, tasks):
    """Sort tasks alphabetically by title."""
    pass

def get_task_statistics(self):
    """
    Get statistics about tasks.
    Returns: Dictionary with counts by status, average priority, etc.
    """
    pass
```

**Data Structure Requirements:**
- Implement at least one sorting algorithm from scratch (merge sort recommended for stability)
- Use appropriate sorting for different use cases
- Maintain sorted views efficiently

---

### Feature 6: Undo/Redo System (20 points)

Implement comprehensive undo/redo for all operations:

```python
def undo(self):
    """
    Undo the last operation.
    Supports: create, update, delete, mark_complete, add_dependency
    Returns: True if successful, False if nothing to undo
    """
    pass

def redo(self):
    """
    Redo the last undone operation.
    Returns: True if successful, False if nothing to redo
    """
    pass

def get_history(self, limit=10):
    """
    Get the recent operation history.
    Returns: List of operation descriptions
    """
    pass
```

**Data Structure Requirements:**
- Use **two stacks** for undo and redo operations
- Store sufficient information to reverse each operation type
- Handle complex operations (e.g., deleting a task with dependencies)

---

### Feature 7: Task History and Analytics (25 points)

Track and analyze task completion patterns:

```python
def get_completed_tasks(self, start_date=None, end_date=None):
    """
    Get completed tasks within a date range.
    Returns: List of completed task objects
    """
    pass

def get_productivity_stats(self, days=7):
    """
    Get productivity statistics for the last N days.
    Returns: Dictionary with tasks completed per day, average priority, etc.
    """
    pass

def get_project_progress(self, project_id):
    """
    Get completion percentage and statistics for a project.
    Returns: Dictionary with total, completed, in_progress counts and percentage
    """
    pass

def get_most_used_tags(self, limit=10):
    """
    Get the most frequently used tags.
    Returns: List of tuples (tag, count) sorted by count
    """
    pass

def estimate_project_completion(self, project_id):
    """
    Estimate when a project will be completed based on current velocity.
    Returns: Estimated date string or "Unknown"
    """
    pass
```

**Data Structure Requirements:**
- Maintain **time-series data** efficiently (array/list with timestamps)
- Use **hash tables** for frequency counting
- Implement efficient aggregation algorithms

---

### Feature 8: Advanced Features (25 points)

Implement at least TWO of these advanced features:

#### Option A: Subtasks (Tree Structure)
```python
def add_subtask(self, parent_task_id, subtask_title, ...):
    """Add a subtask to an existing task."""
    pass

def get_task_tree(self, root_task_id):
    """Get the entire tree of tasks and subtasks."""
    pass

def complete_task_tree(self, root_task_id):
    """Mark a task and all its subtasks as complete."""
    pass
```
**Requires:** Tree data structure with parent-child relationships

#### Option B: Recurring Tasks
```python
def create_recurring_task(self, title, recurrence_pattern, ...):
    """Create a task that repeats (daily, weekly, monthly)."""
    pass

def generate_recurring_instances(self, days_ahead=30):
    """Generate task instances for recurring tasks."""
    pass
```
**Requires:** Efficient date handling and task generation algorithms

#### Option C: Task Templates
```python
def save_task_template(self, template_name, task_structure):
    """Save a task or project structure as a reusable template."""
    pass

def create_from_template(self, template_name, **kwargs):
    """Create new tasks from a saved template."""
    pass
```
**Requires:** Deep copying of task structures, hash table for template storage

#### Option D: Collaborative Features
```python
def assign_task(self, task_id, user_id):
    """Assign a task to a user."""
    pass

def get_user_tasks(self, user_id):
    """Get all tasks assigned to a specific user."""
    pass

def get_user_workload(self, user_id):
    """Calculate total priority points assigned to a user."""
    pass
```
**Requires:** User management with hash tables, task assignment tracking

---

## Implementation Requirements

### Required Data Structures (Must Use At Least 5)

1. ✅ **Hash Tables** - For O(1) lookups (tasks by ID, tags, projects)
2. ✅ **Graphs** - For task dependencies and dependency analysis
3. ✅ **Heaps/Priority Queues** - For priority-based task scheduling
4. ✅ **Stacks** - For undo/redo functionality
5. ✅ **Trees** - For subtask hierarchies (if implementing subtasks)
6. ⚪ **Arrays/Lists** - For storing and sorting tasks
7. ⚪ **Linked Lists** - Optional, for maintaining task order or history

### Required Algorithms (Must Implement At Least 3)

1. ✅ **Sorting Algorithm** - Merge sort or quick sort for task sorting
2. ✅ **Graph Traversal** - DFS or BFS for dependency checking
3. ✅ **Topological Sort** - For valid task ordering
4. ⚪ **Search Algorithm** - Binary search for date ranges (if applicable)
5. ⚪ **Cycle Detection** - For preventing circular dependencies

---

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| **Feature 1: Task Management** | 30 | Correctness (15), Efficiency (10), Code quality (5) |
| **Feature 2: Dependencies (Graph)** | 30 | Graph implementation (15), Topological sort (10), Cycle detection (5) |
| **Feature 3: Priority Queue** | 25 | Priority queue implementation (15), Scheduling logic (10) |
| **Feature 4: Search & Filtering** | 25 | Correctness (15), Efficiency (7), Multiple criteria (3) |
| **Feature 5: Sorting** | 20 | Sorting implementation (12), Multiple sort options (8) |
| **Feature 6: Undo/Redo** | 20 | Correctness (12), Comprehensive coverage (8) |
| **Feature 7: Analytics** | 25 | Implementation (15), Useful insights (10) |
| **Feature 8: Advanced Features** | 25 | Two features fully implemented and tested |
| **Documentation** | 20 | README (5), Code comments (5), Complexity analysis (10) |
| **Testing** | 20 | Test coverage (10), Edge cases (5), Integration tests (5) |
| **Code Quality** | 10 | Clean code (5), Good structure (3), Error handling (2) |
| **Total** | 200 | |

---

## Deliverables

### 1. Source Code
- `task_manager.py` - Main implementation file
- `data_structures.py` - Custom data structure implementations (if any)
- `utils.py` - Helper functions and utilities
- `test_task_manager.py` - Comprehensive test suite

### 2. Documentation
- `README.md` - Project overview, setup instructions, usage examples
- `DESIGN.md` - Design decisions, data structure choices, complexity analysis
- `API.md` - Complete API documentation for all methods

### 3. Analysis Document
Create `final_project_analysis.md` including:

#### Data Structure Justification (8 points)
- List each data structure used
- Explain why you chose it for that specific feature
- Discuss alternatives and why you didn't use them

#### Complexity Analysis (7 points)
- Provide time and space complexity for all major operations
- Explain any trade-offs you made
- Identify bottlenecks and optimization opportunities

#### Testing Strategy (5 points)
- Describe your testing approach
- List key test cases and edge cases
- Document any known limitations

---

## Timeline Suggestion

### Week 1: Foundation (20-25 hours)
- **Days 1-2**: Design system architecture, choose data structures
- **Days 3-4**: Implement Features 1 & 2 (Task Management, Dependencies)
- **Days 5-7**: Implement Features 3 & 4 (Priority Queue, Search)

### Week 2: Core Features (15-20 hours)
- **Days 8-9**: Implement Features 5 & 6 (Sorting, Undo/Redo)
- **Days 10-11**: Implement Feature 7 (Analytics)
- **Days 12-14**: Implement Feature 8 (Advanced features - 2 options)

### Week 3: Polish & Documentation (8-12 hours)
- **Days 15-16**: Write comprehensive tests
- **Days 17-18**: Write documentation
- **Days 19-20**: Code cleanup, optimization, final testing
- **Day 21**: Final review and submission

---

## Starter Code

```python
"""
Task Management System - Final Project
A comprehensive task manager demonstrating mastery of data structures and algorithms.
"""

from datetime import datetime, timedelta
from collections import defaultdict, deque
import heapq

class Task:
    """Represents a task with all required attributes."""
    def __init__(self, task_id, title, description, priority, due_date, project_id, tags=None):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.priority = priority  # 1-5, 5 is highest
        self.status = "todo"  # todo, in_progress, completed, blocked
        self.due_date = due_date
        self.project_id = project_id
        self.tags = tags or []
        self.dependencies = []  # List of task_ids
        self.created_at = datetime.now()
        self.completed_at = None
    
    def __repr__(self):
        return f"Task({self.task_id}, '{self.title}', priority={self.priority}, status={self.status})"
    
    def __lt__(self, other):
        """For heap operations - higher priority = lower value (max heap simulation)."""
        return self.priority > other.priority

class TaskManager:
    """Main task management system."""
    
    def __init__(self):
        # TODO: Initialize your data structures
        self.tasks = {}  # Hash table: task_id -> Task
        self.next_task_id = 1
        
        # TODO: Add more data structures for:
        # - Tag indexing
        # - Project indexing
        # - Dependency graph
        # - Priority queue
        # - Undo/redo stacks
        # - Analytics tracking
    
    def create_task(self, title, description, priority, due_date, project_id, tags=None):
        """Create a new task."""
        # TODO: Implement
        pass
    
    # TODO: Implement all other required methods

def main():
    """Example usage of the task management system."""
    tm = TaskManager()
    
    # Create some tasks
    task1 = tm.create_task(
        "Design database schema",
        "Create ER diagram and schema for the project",
        priority=5,
        due_date="2024-02-15",
        project_id="website-redesign",
        tags=["backend", "database"]
    )
    
    task2 = tm.create_task(
        "Implement API endpoints",
        "Create REST API endpoints for task management",
        priority=4,
        due_date="2024-02-20",
        project_id="website-redesign",
        tags=["backend", "api"]
    )
    
    # Add dependency: task2 depends on task1
    tm.add_dependency(task2, task1)
    
    # Get task order
    order = tm.get_task_order()
    print(f"Task completion order: {order}")
    
    # Get next task to work on
    next_task = tm.get_next_task()
    print(f"Next task: {next_task}")
    
    # Filter and search
    backend_tasks = tm.search_tasks_by_tag("backend")
    print(f"Backend tasks: {backend_tasks}")

if __name__ == "__main__":
    main()
```

---

## Testing Requirements

Create comprehensive tests including:

### Unit Tests
- Test each method individually
- Test with valid inputs
- Test with invalid inputs
- Test edge cases (empty, null, boundary values)

### Integration Tests
- Test interactions between features
- Test dependency chains
- Test undo/redo with complex operations
- Test filtering with multiple criteria

### Performance Tests
- Test with large datasets (1000+ tasks)
- Verify O(1), O(log n), and O(n) operations meet requirements
- Test worst-case scenarios

### Example Test Cases
```python
def test_create_task():
    """Test basic task creation."""
    tm = TaskManager()
    task_id = tm.create_task("Test", "Description", 3, "2024-12-31", "proj1")
    assert task_id is not None
    assert tm.get_task(task_id).title == "Test"

def test_circular_dependency_detection():
    """Test that circular dependencies are prevented."""
    tm = TaskManager()
    task1 = tm.create_task("A", "", 1, "2024-12-31", "proj1")
    task2 = tm.create_task("B", "", 1, "2024-12-31", "proj1")
    tm.add_dependency(task2, task1)  # B depends on A
    with pytest.raises(CircularDependencyError):
        tm.add_dependency(task1, task2)  # A depends on B - should fail

def test_priority_queue_ordering():
    """Test that tasks are retrieved in priority order."""
    tm = TaskManager()
    # Create tasks with different priorities
    # Verify get_next_task returns highest priority available task
```

---

## Tips for Success

1. **Plan First**: Spend time designing your system before coding
2. **Start Simple**: Implement basic features first, then add complexity
3. **Test Continuously**: Write tests as you implement features
4. **Optimize Later**: Get it working correctly first, then optimize
5. **Document As You Go**: Don't leave documentation for the end
6. **Use Version Control**: Commit frequently with meaningful messages
7. **Ask for Help**: If stuck for more than an hour, ask questions

---

## Common Challenges

### Challenge 1: Managing Dependencies
- **Solution**: Use an adjacency list representation
- **Tip**: Draw the graph on paper first

### Challenge 2: Efficient Tag Lookup
- **Solution**: Maintain a hash table mapping tags to lists of task IDs
- **Tip**: Update this index whenever tasks are added/deleted/modified

### Challenge 3: Priority Queue with Dynamic Priorities
- **Solution**: Recalculate priority scores when needed, or rebuild heap
- **Tip**: Consider when to update vs. rebuild based on operation frequency

### Challenge 4: Comprehensive Undo/Redo
- **Solution**: Store operation type and all data needed for reversal
- **Tip**: Test undo/redo extensively with different operation sequences

---

## Extension Ideas (Optional)

Want to go beyond? Try these:
- Build a command-line interface (CLI)
- Build a web API using Flask or FastAPI
- Add data persistence (save/load from files or database)
- Implement real-time notifications for due dates
- Add task time estimates and track time spent
- Implement a Kanban board view
- Add support for task comments and attachments

---

## Evaluation Criteria

Your project will be evaluated on:

### Functionality (40%)
- All required features work correctly
- Edge cases are handled properly
- System behaves as expected

### Data Structure Usage (25%)
- At least 5 different data structures used appropriately
- Complexity requirements are met
- Efficient algorithms implemented

### Code Quality (15%)
- Clean, readable, well-organized code
- Proper error handling
- Good variable/function names
- Follows Python conventions (PEP 8)

### Testing (10%)
- Comprehensive test coverage
- Edge cases tested
- Integration tests included

### Documentation (10%)
- Clear README with setup and usage
- Design decisions explained
- Complexity analysis provided
- Code comments where needed

---

## Submission

Submit via your course platform:
1. Zip file containing all source code and documentation
2. Name: `lastname_firstname_final_project.zip`
3. Include a `requirements.txt` if using external libraries
4. Include instructions to run your tests

---

## Academic Integrity

This is an individual project. You may:
- ✅ Consult course materials and documentation
- ✅ Use Python standard library
- ✅ Discuss high-level design concepts with peers
- ✅ Ask instructor/TA for clarification

You may not:
- ❌ Share code with other students
- ❌ Use code from online sources without proper citation
- ❌ Submit work that is not your own
- ❌ Use AI code generation tools to write significant portions

---

## Questions?

**Office Hours**: Schedule time with your instructor to discuss:
- Design decisions
- Algorithm choices
- Implementation challenges
- Optimization strategies

**Discussion Forum**: Post questions about:
- Requirement clarifications
- Testing strategies
- General approach

**Email**: For private concerns or questions

---

**This is your chance to showcase everything you've learned. Build something you're proud of!**

**Good luck! 🚀**
