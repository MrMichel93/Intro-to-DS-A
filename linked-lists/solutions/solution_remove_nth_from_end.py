"""Solution: Remove Nth From End (Challenge 4)
Two-pointer technique with n-gap."""

def remove_nth_from_end(head, n):
    """Remove nth node from end. O(n) time, O(1) space."""
    dummy = ListNode(0, head)
    fast = slow = dummy
    
    # Move fast n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next
    
    # Move both until fast reaches end
    while fast:
        fast = fast.next
        slow = slow.next
    
    # Remove nth node
    slow.next = slow.next.next
    return dummy.next
