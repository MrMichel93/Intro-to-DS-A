'''Solution: Generate Binary Numbers (Challenge 2)
Generate binary representations using queue.'''

from collections import deque

def generate_binary(n):
    result = []
    queue = deque(['1'])
    for _ in range(n):
        binary = queue.popleft()
        result.append(binary)
        queue.append(binary + '0')
        queue.append(binary + '1')
    return result
