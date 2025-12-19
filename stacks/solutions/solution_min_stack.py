"""
Solution: Min Stack (Challenge 2)

Problem: Design a stack supporting O(1) getMin operation.
Demonstrates auxiliary data structure pattern.
"""


class MinStack:
    """
    Stack with O(1) minimum retrieval using auxiliary stack.
    
    Approach: Maintain two synchronized stacks:
    - Main stack: stores all values
    - Min stack: stores minimum value at each level
    
    Time Complexity: O(1) for all operations
    Space Complexity: O(n) for both stacks
    """
    
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val):
        self.stack.append(val)
        # Push current minimum (either new val or previous min)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))
    
    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.min_stack[-1]


if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print(f"Min: {ms.getMin()}")  # -3
    ms.pop()
    print(f"Top: {ms.top()}")  # 0
    print(f"Min: {ms.getMin()}")  # -2
