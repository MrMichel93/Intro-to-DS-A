'''Solution: Task Scheduler (Challenge 5)
Schedule tasks with cooldown periods.'''

from collections import Counter
import heapq

def least_interval(tasks, n):
    counts = Counter(tasks)
    max_heap = [-cnt for cnt in counts.values()]
    heapq.heapify(max_heap)
    time = 0
    
    while max_heap:
        temp = []
        for _ in range(n + 1):
            if max_heap:
                temp.append(heapq.heappop(max_heap))
        for cnt in temp:
            if cnt + 1 < 0:
                heapq.heappush(max_heap, cnt + 1)
        time += len(temp) if max_heap else len([c for c in temp if c < 0])
    return time
