# Midterm Challenge: Building a Contact Management System

**Due After Completing Module 5: Hash Tables**  
**Time Estimate:** 3-4 hours  
**Total Points:** 100

---

## Overview

You will build a **Contact Management System** that demonstrates your understanding of data structures from Modules 0-5. This is a comprehensive challenge that requires you to apply multiple concepts including arrays, linked lists, stacks, queues, and hash tables.

## Learning Objectives

By completing this challenge, you will demonstrate:
- ✅ Understanding of when to use different data structures
- ✅ Ability to implement efficient search and retrieval operations
- ✅ Skills in managing data with proper time complexity considerations
- ✅ Practical application of hash tables for fast lookups
- ✅ Understanding of undo/redo functionality using stacks
- ✅ Knowledge of queue-based task processing

---

## Problem Statement

Create a contact management system that allows users to:
1. Add, delete, and search for contacts
2. Maintain contact history with undo/redo functionality
3. Process bulk operations using a queue
4. Efficiently search contacts by different attributes
5. Keep track of frequently accessed contacts

---

## Requirements

### Part 1: Core Contact Management (30 points)

Implement a `ContactManager` class with the following functionality:

#### Contact Structure
Each contact should have:
- `id`: Unique identifier (integer)
- `name`: Contact name (string)
- `phone`: Phone number (string)
- `email`: Email address (string)
- `category`: Category like "work", "family", "friends" (string)

#### Required Methods

```python
class ContactManager:
    def __init__(self):
        """Initialize the contact manager with appropriate data structures"""
        pass
    
    def add_contact(self, name, phone, email, category):
        """
        Add a new contact. Auto-generate unique ID.
        Time Complexity Requirement: O(1) average case
        Returns: contact_id
        """
        pass
    
    def delete_contact(self, contact_id):
        """
        Delete a contact by ID.
        Time Complexity Requirement: O(1) average case
        Returns: True if deleted, False if not found
        """
        pass
    
    def search_by_name(self, name):
        """
        Search for contacts by name (exact match).
        Time Complexity Requirement: O(1) average case
        Returns: Contact object or None
        """
        pass
    
    def search_by_phone(self, phone):
        """
        Search for contacts by phone number.
        Time Complexity Requirement: O(1) average case
        Returns: Contact object or None
        """
        pass
    
    def get_contacts_by_category(self, category):
        """
        Get all contacts in a specific category.
        Time Complexity Requirement: O(k) where k is the number of contacts in category
        Returns: List of contact objects
        """
        pass
    
    def get_all_contacts(self):
        """
        Get all contacts sorted by name.
        Returns: List of all contact objects
        """
        pass
```

**Hints for Part 1:**
- Use hash tables (dictionaries) for O(1) lookups
- Consider maintaining multiple hash tables for different search keys
- Use an array or list to maintain contacts by category

---

### Part 2: Undo/Redo Functionality (25 points)

Implement undo and redo operations for add and delete actions:

```python
def undo(self):
    """
    Undo the last operation (add or delete).
    Time Complexity Requirement: O(1)
    Returns: True if undo successful, False if nothing to undo
    """
    pass

def redo(self):
    """
    Redo the last undone operation.
    Time Complexity Requirement: O(1)
    Returns: True if redo successful, False if nothing to redo
    """
    pass
```

**Requirements:**
- Support unlimited undo/redo operations
- When a new operation is performed, clear the redo stack
- Store enough information to reverse operations

**Hints for Part 2:**
- Use two stacks: one for undo history, one for redo history
- Store operation type and relevant data needed to reverse it
- Example: For add_contact, store ("add", contact_id); for delete, store ("delete", contact_object)

---

### Part 3: Bulk Operations Queue (20 points)

Implement a queue-based system for bulk contact operations:

```python
def queue_bulk_add(self, contacts_list):
    """
    Queue multiple contacts to be added.
    contacts_list: List of tuples [(name, phone, email, category), ...]
    """
    pass

def queue_bulk_delete(self, contact_ids):
    """
    Queue multiple contact IDs to be deleted.
    contact_ids: List of contact IDs
    """
    pass

def process_queue(self, max_operations=None):
    """
    Process queued operations in FIFO order.
    max_operations: Maximum number of operations to process (None = all)
    Returns: Number of operations processed
    """
    pass

def get_queue_size(self):
    """
    Get the number of pending operations.
    Returns: Integer count
    """
    pass
```

**Requirements:**
- Operations should be processed in the order they were queued
- Support processing a limited number of operations at a time
- Each queued operation should count as a separate undo-able action

**Hints for Part 3:**
- Use a queue (collections.deque in Python)
- Store operation type and data in the queue
- Process operations one at a time, integrating with undo functionality

---

### Part 4: Recently Accessed Contacts (15 points)

Implement functionality to track and retrieve recently accessed contacts:

```python
def access_contact(self, contact_id):
    """
    Mark a contact as accessed (for tracking recent contacts).
    Returns: Contact object or None
    """
    pass

def get_recent_contacts(self, limit=5):
    """
    Get the most recently accessed contacts.
    limit: Maximum number of contacts to return
    Returns: List of contact objects (most recent first)
    """
    pass
```

**Requirements:**
- Track the order of contact accesses
- Return the most recently accessed contacts
- If a contact is accessed multiple times, it should appear only once (at its most recent position)

**Hints for Part 4:**
- Use a linked list or deque to maintain access order
- Use a hash table to track if a contact is already in the recent list
- When a contact is accessed again, move it to the front

---

### Part 5: Analysis and Documentation (10 points)

Create a document called `midterm_analysis.md` that includes:

1. **Data Structure Choices** (4 points)
   - Explain which data structures you used for each feature
   - Justify your choices based on time/space complexity requirements

2. **Complexity Analysis** (3 points)
   - Provide time and space complexity for each major operation
   - Explain any trade-offs you made

3. **Testing Strategy** (3 points)
   - Describe how you tested your implementation
   - List edge cases you considered

---

## Starter Code

```python
from collections import deque

class Contact:
    """Represents a contact with id, name, phone, email, and category."""
    def __init__(self, contact_id, name, phone, email, category):
        self.id = contact_id
        self.name = name
        self.phone = phone
        self.email = email
        self.category = category
    
    def __repr__(self):
        return f"Contact({self.id}, {self.name}, {self.phone}, {self.email}, {self.category})"

class ContactManager:
    def __init__(self):
        # TODO: Initialize your data structures here
        self.next_id = 1
        # Add more initialization as needed
    
    # TODO: Implement all required methods

# Example usage
if __name__ == "__main__":
    cm = ContactManager()
    
    # Add contacts
    id1 = cm.add_contact("Alice Smith", "555-1234", "alice@email.com", "work")
    id2 = cm.add_contact("Bob Jones", "555-5678", "bob@email.com", "friends")
    
    # Search
    contact = cm.search_by_name("Alice Smith")
    print(contact)
    
    # Undo/Redo
    cm.delete_contact(id1)
    cm.undo()  # Restores Alice
    
    # Bulk operations
    cm.queue_bulk_add([
        ("Charlie Brown", "555-9999", "charlie@email.com", "family"),
        ("Diana Prince", "555-0000", "diana@email.com", "work")
    ])
    cm.process_queue()
    
    # Recent contacts
    cm.access_contact(id1)
    cm.access_contact(id2)
    recent = cm.get_recent_contacts(5)
    print("Recent:", recent)
```

---

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| **Part 1: Core Management** | 30 | Correctness (15), Time complexity (10), Code quality (5) |
| **Part 2: Undo/Redo** | 25 | Correctness (15), Proper stack usage (7), Edge cases (3) |
| **Part 3: Bulk Operations** | 20 | Correctness (12), Queue implementation (5), Integration (3) |
| **Part 4: Recent Contacts** | 15 | Correctness (10), Efficiency (5) |
| **Part 5: Documentation** | 10 | Completeness (5), Clarity (3), Analysis depth (2) |
| **Total** | 100 | |

---

## Submission Requirements

1. **Code**: Submit `contact_manager.py` with your implementation
2. **Analysis**: Submit `midterm_analysis.md` with your documentation
3. **Tests**: Submit `test_contact_manager.py` with test cases (recommended)

---

## Tips for Success

1. **Start with the data structures**: Plan which data structures you'll use before coding
2. **Implement incrementally**: Build one part at a time and test as you go
3. **Focus on complexity**: Make sure your operations meet the time complexity requirements
4. **Handle edge cases**: Empty inputs, duplicate contacts, invalid IDs, etc.
5. **Test thoroughly**: Write comprehensive tests before submitting

---

## Extension Ideas (Optional Bonus)

If you finish early and want extra practice:
- Add support for updating contact information
- Implement a "favorites" feature using a hash set
- Add name substring search (not just exact match)
- Export contacts to a file and import them back
- Add contact groups with many-to-many relationships

---

## Common Pitfalls to Avoid

❌ **Don't**: Use linear search (O(n)) when you should use hash tables (O(1))  
❌ **Don't**: Forget to update all relevant data structures when adding/deleting  
❌ **Don't**: Implement undo/redo using arrays with O(n) operations  
❌ **Don't**: Process the queue in the wrong order (it should be FIFO)

✅ **Do**: Use multiple hash tables for different search keys  
✅ **Do**: Use stacks for undo/redo (LIFO operations)  
✅ **Do**: Use a queue for bulk operations (FIFO processing)  
✅ **Do**: Test edge cases like empty operations and duplicate data

---

## Questions?

If you have questions about requirements:
- Review the relevant module READMEs (Modules 0-5)
- Check the time complexity requirements carefully
- Consider what data structure naturally fits each operation
- Ask your instructor for clarification if needed

**Good luck! This challenge will solidify your understanding of fundamental data structures.**
