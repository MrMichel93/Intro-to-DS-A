# Problem 1: Valid Parentheses

**Difficulty:** Easy 🟢

## Problem Statement

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. A string is valid if:
- Open brackets are closed by the same type of brackets
- Open brackets are closed in the correct order

### Examples:
```
Input: "()"
Output: true

Input: "()[]{}"
Output: true

Input: "(]"
Output: false

Input: "([)]"
Output: false

Input: "{[]}"
Output: true
```

## Solution

<details>
<summary>Click to reveal solution</summary>

```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:  # Closing bracket
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:  # Opening bracket
            stack.append(char)
    
    return len(stack) == 0

# Time: O(n), Space: O(n)
```

</details>

[← Back to Stacks](./README.md) | [Next Problem →](./problem2.md)
