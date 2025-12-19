"""Solution: Merge Two Sorted Lists (Challenge 3)
Demonstrates merge operation on sorted lists."""

def merge_two_lists(list1, list2):
    """Merge two sorted lists. O(n+m) time, O(1) space."""
    dummy = ListNode(0)
    tail = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    tail.next = list1 if list1 else list2
    return dummy.next
