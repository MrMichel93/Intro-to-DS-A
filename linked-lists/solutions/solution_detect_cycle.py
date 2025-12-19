"""Solution: Detect Cycle (Challenge 2)
Floyd's Tortoise and Hare algorithm."""

def has_cycle(head):
    """Detect cycle using two pointers. O(n) time, O(1) space."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
