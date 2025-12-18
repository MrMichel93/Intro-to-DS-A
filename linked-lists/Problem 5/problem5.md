# Problem 5: Remove Nth Node From End

**Difficulty:** Medium 🟡

## Problem Statement

Remove the nth node from the end of a linked list and return the head.

### Example:
```
Input: 1 → 2 → 3 → 4 → 5 → null, n = 2
Output: 1 → 2 → 3 → 5 → null
(Remove the 2nd node from end, which is 4)
```

## Hints

<details>
<summary>Hint</summary>
Use two pointers with n nodes gap between them!
</details>

## Solution

<details>
<summary>Click to reveal solution</summary>

```python
def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    first = dummy
    second = dummy
    
    # Move first pointer n+1 steps ahead
    for _ in range(n + 1):
        first = first.next
    
    # Move both pointers until first reaches end
    while first:
        first = first.next
        second = second.next
    
    # Remove the nth node
    second.next = second.next.next
    
    return dummy.next

# Time: O(n), Space: O(1)
```

</details>

[← Previous Problem](./problem4.md) | [Back to Linked Lists](./README.md) | [Next Problem →](./problem6.md)
