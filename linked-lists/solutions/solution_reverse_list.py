"""Solution: Reverse Linked List (Challenge 1)
Demonstrates iterative and recursive reversal."""

def reverse_list(head):
    """Reverse linked list iteratively. O(n) time, O(1) space."""
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def reverse_list_recursive(head):
    """Reverse linked list recursively. O(n) time, O(n) space for call stack."""
    if not head or not head.next:
        return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head
