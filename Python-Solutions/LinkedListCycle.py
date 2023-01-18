from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # To detect a cycle, we have two main options: Iterate through the list, adding each node
    # to a set. If we encounter a node that is already in the set, we know we have a cycle.
    # This uses O(n) space, where n is the number of nodes in the list as wel as O(n) time.
    # We can also use two pointers, one fast and one slow. The fast pointer moves two nodes
    # at a time, while the slow pointer moves one node at a time. If the fast pointer ever
    # catches up to the slow pointer, we know we have a cycle. This uses O(1) space and O(n)
    # time.
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = slow.next
        while slow and fast and slow.next and fast.next and fast.next.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False