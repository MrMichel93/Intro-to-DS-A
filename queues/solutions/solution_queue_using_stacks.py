'''Solution: Implement Queue using Stacks (Challenge 1)
Demonstrates queue operations using two stacks.'''

class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    
    def push(self, x):
        self.stack_in.append(x)
    
    def pop(self):
        self._move()
        return self.stack_out.pop()
    
    def peek(self):
        self._move()
        return self.stack_out[-1]
    
    def _move(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
