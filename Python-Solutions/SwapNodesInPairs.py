from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # The idea is to use a dummy node to point to the head of the list.
    # Start by setting the previous node to the dummy node. Then, we iterate through the list
    # and swap the first node with the second node. Then, we set the previous node to the first node
    # and set the head to the next node.
    # We swap the nodes by setting the previous node's next to the second node, the first node's next
    # to the second node's next, and the second node's next to the first node. We then set the previous
    # node to the first node and set the head to the first node's next.
    # Time Complexity: O(n) where n is the number of nodes in the list
    # Space Complexity: O(1)
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_node = dummy
        while head and head.next:
            first_node = head;
            second_node = head.next;
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            prev_node = first_node
            head = first_node.next
        return dummy.next