"""
Solution: Basic Calculator (Challenge 6)

Problem: Evaluate expression with parentheses, addition, subtraction.
Complex stack-based parsing with state management.
"""


def calculate(s):
    """
    Evaluate mathematical expression with parentheses.
    
    Approach: Use stack to save state when entering parentheses.
    Track current result, sign, and number being built.
    
    Time Complexity: O(n) - single pass
    Space Complexity: O(n) - stack for nested parentheses
    
    Examples:
    >>> calculate("1 + 1")
    2
    >>> calculate(" 2-1 + 2 ")
    3
    >>> calculate("(1+(4+5+2)-3)+(6+8)")
    23
    """
    stack = []
    result = 0
    number = 0
    sign = 1  # 1 for positive, -1 for negative
    
    for char in s:
        if char.isdigit():
            number = number * 10 + int(char)
        elif char == '+':
            result += sign * number
            number = 0
            sign = 1
        elif char == '-':
            result += sign * number
            number = 0
            sign = -1
        elif char == '(':
            # Push current result and sign onto stack
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            result += sign * number
            number = 0
            # Pop sign and previous result
            result *= stack.pop()  # Apply sign before parentheses
            result += stack.pop()  # Add result before parentheses
    
    result += sign * number
    return result


if __name__ == "__main__":
    tests = [
        ("1 + 1", 2),
        (" 2-1 + 2 ", 3),
        ("(1+(4+5+2)-3)+(6+8)", 23),
        ("2-(5-6)", 3)
    ]
    for expr, expected in tests:
        result = calculate(expr)
        print(f"'{expr}' = {result} (expected {expected})")
