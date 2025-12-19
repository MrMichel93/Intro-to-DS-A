"""
Solution: Evaluate Reverse Polish Notation (Challenge 4)

Problem: Evaluate arithmetic expression in postfix notation.
Demonstrates stack-based expression evaluation.
"""


def eval_rpn(tokens):
    """
    Evaluate RPN expression using stack.
    
    Approach: Push numbers onto stack. When operator found,
    pop two operands, apply operation, push result.
    
    Time Complexity: O(n) - process each token once
    Space Complexity: O(n) - stack size
    
    Examples:
    >>> eval_rpn(["2", "1", "+", "3", "*"])
    9
    """
    stack = []
    operators = {'+', '-', '*', '/'}
    
    for token in tokens:
        if token in operators:
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


if __name__ == "__main__":
    tests = [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6)
    ]
    for tokens, expected in tests:
        result = eval_rpn(tokens)
        print(f"{tokens} = {result} (expected {expected})")
