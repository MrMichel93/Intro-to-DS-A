# Problem 3: Middle of Linked List

**Difficulty:** Medium 🟡

## Problem Statement

Find the middle node of a linked list. If there are two middle nodes, return the second one.

### Example 1:
```
Input: 1 → 2 → 3 → 4 → 5 → null
Output: Node with value 3
```

### Example 2:
```
Input: 1 → 2 → 3 → 4 → 5 → 6 → null
Output: Node with value 4
```

## Solution

<details>
<summary>Click to reveal solution</summary>

```python
def find_middle(head):
    """Use slow and fast pointers"""
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow  # When fast reaches end, slow is at middle

# Time: O(n), Space: O(1)
```

</details>

[← Previous Problem](./problem2.md) | [Back to Linked Lists](./README.md) | [Next Problem →](./problem4.md)
