'''Solution: Sliding Window Maximum (Challenge 3)
Find maximum in each sliding window using deque.'''

from collections import deque

def max_sliding_window(nums, k):
    deq = deque()
    result = []
    for i, num in enumerate(nums):
        while deq and nums[deq[-1]] < num:
            deq.pop()
        deq.append(i)
        if deq[0] == i - k:
            deq.popleft()
        if i >= k - 1:
            result.append(nums[deq[0]])
    return result
