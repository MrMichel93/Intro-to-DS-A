"""
Solution: Valid Parentheses (Challenge 1)

Problem: Determine if a string of brackets is valid and properly balanced.
Classic stack problem demonstrating LIFO for matching pairs.
"""


def is_valid(s):
    """
    Check if brackets are balanced using a stack.
    
    Approach: Push opening brackets onto stack. For closing brackets,
    check if they match the most recent opening bracket (stack top).
    
    Time Complexity: O(n) - single pass
    Space Complexity: O(n) - stack in worst case stores n/2 brackets
    
    Examples:
    >>> is_valid("()")
    True
    >>> is_valid("()[]{}")
    True
    >>> is_valid("(]")
    False
    """
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in brackets:  # Closing bracket
            if not stack or stack[-1] != brackets[char]:
                return False
            stack.pop()
        else:  # Opening bracket
            stack.append(char)
    
    return len(stack) == 0


if __name__ == "__main__":
    tests = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    for test in tests:
        print(f"{test}: {is_valid(test)}")
