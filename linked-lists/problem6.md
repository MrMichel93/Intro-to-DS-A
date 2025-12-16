# Problem 6: Add Two Numbers

**Difficulty:** Hard 🔴

## Problem Statement

You are given two linked lists representing two non-negative integers. The digits are stored in reverse order. Add the two numbers and return the sum as a linked list.

### Example:
```
Input: 
  (2 → 4 → 3) represents 342
  (5 → 6 → 4) represents 465
Output: 7 → 0 → 8 (represents 807)
Explanation: 342 + 465 = 807
```

## Solution

<details>
<summary>Click to reveal solution</summary>

```python
def add_two_numbers(l1, l2):
    dummy = Node(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.data if l1 else 0
        val2 = l2.data if l2 else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10
        
        current.next = Node(digit)
        current = current.next
        
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return dummy.next

# Time: O(max(m, n)), Space: O(max(m, n))
```

</details>

[← Previous Problem](./problem5.md) | [Back to Linked Lists](./README.md)
