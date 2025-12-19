"""Solution: Merge K Sorted Lists (Challenge 6)
Uses min-heap for efficient k-way merge."""

import heapq

def merge_k_lists(lists):
    """Merge k sorted lists. O(n log k) time, O(k) space."""
    heap = []
    
    # Add first node from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))
    
    dummy = ListNode(0)
    tail = dummy
    
    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next
