# Problem 3: Evaluate Postfix Expression

**Difficulty:** Medium 🟡

## Problem Statement

Evaluate a postfix (Reverse Polish Notation) expression. Valid operators are +, -, *, /. Each operand may be an integer or another expression.

### Examples:
```
Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

## Solution

<details>
<summary>Click to reveal solution</summary>

```python
def eval_rpn(tokens):
    stack = []
    
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            else:  # division
                result = int(a / b)  # Truncate toward zero
            
            stack.append(result)
        else:
            stack.append(int(token))
    
    return stack[0]

# Time: O(n), Space: O(n)
```

</details>

[← Previous Problem](./problem2.md) | [Back to Stacks](./README.md) | [Next Problem →](./problem4.md)
