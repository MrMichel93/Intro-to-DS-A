# Problem 2: Detect Cycle in Linked List

**Difficulty:** Easy 🟢

## Problem Statement

Determine if a linked list has a cycle. A cycle exists if a node can be reached again by following the next pointers.

### Example 1:
```
Input: 1 → 2 → 3 → 4 → 2 (back to node with value 2)
Output: true
```

### Example 2:
```
Input: 1 → 2 → 3 → null
Output: false
```

## Hints

<details>
<summary>Hint 1</summary>
Floyd's Cycle Detection: Use two pointers moving at different speeds!
</details>

<details>
<summary>Hint 2</summary>
If there's a cycle, the fast pointer will eventually catch up to the slow pointer.
</details>

## Solution

<details>
<summary>Click to reveal solution</summary>

```python
def has_cycle(head):
    """Floyd's Tortoise and Hare algorithm"""
    if not head:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next        # Move 1 step
        fast = fast.next.next   # Move 2 steps
        
        if slow == fast:
            return True  # They met, cycle exists!
    
    return False  # Fast reached end, no cycle

# Time: O(n), Space: O(1)
```

</details>

[← Previous Problem](./problem1.md) | [Back to Linked Lists](./README.md) | [Next Problem →](./problem3.md)
