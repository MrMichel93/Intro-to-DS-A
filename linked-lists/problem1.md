# Problem 1: Reverse a Linked List

**Difficulty:** Easy 🟢

## Problem Statement

Reverse a singly linked list and return the new head.

### Example:
```
Input:  1 → 2 → 3 → 4 → 5 → null
Output: 5 → 4 → 3 → 2 → 1 → null
```

## Hints

<details>
<summary>Hint 1</summary>
You need to change the direction of all the "next" pointers.
</details>

<details>
<summary>Hint 2</summary>
Use three pointers: previous, current, and next.
</details>

## Solution

<details>
<summary>Click to reveal solution</summary>

```python
def reverse_list(head):
    prev = None
    current = head
    
    while current:
        # Save next node
        next_node = current.next
        # Reverse the pointer
        current.next = prev
        # Move pointers forward
        prev = current
        current = next_node
    
    return prev  # New head

# Time: O(n), Space: O(1)
```

</details>

[← Back to Linked Lists](./README.md) | [Next Problem →](./problem2.md)
