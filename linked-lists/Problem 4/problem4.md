# Problem 4: Merge Two Sorted Lists

**Difficulty:** Medium 🟡

## Problem Statement

Merge two sorted linked lists into one sorted linked list.

### Example:
```
Input: 
  List 1: 1 → 2 → 4 → null
  List 2: 1 → 3 → 4 → null
Output: 1 → 1 → 2 → 3 → 4 → 4 → null
```

## Solution

<details>
<summary>Click to reveal solution</summary>

```python
def merge_two_lists(l1, l2):
    dummy = Node(0)  # Dummy node to simplify logic
    current = dummy
    
    while l1 and l2:
        if l1.data <= l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # Attach remaining nodes
    current.next = l1 if l1 else l2
    
    return dummy.next  # Skip dummy node

# Time: O(n + m), Space: O(1)
```

</details>

[← Previous Problem](./problem3.md) | [Back to Linked Lists](./README.md) | [Next Problem →](./problem5.md)
