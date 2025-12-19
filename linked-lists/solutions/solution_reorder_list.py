"""Solution: Reorder List (Challenge 5)
Three-step approach: find middle, reverse, merge."""

def reorder_list(head):
    """Reorder list in-place. O(n) time, O(1) space."""
    if not head or not head.next:
        return
    
    # Find middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    second = slow.next
    slow.next = None
    prev = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp
    
    # Merge alternately
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2
