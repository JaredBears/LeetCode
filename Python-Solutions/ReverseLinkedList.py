from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution: #IMPROVED OVER THE OLD SOLUTION :) 
    # Time Complexity: O(N) where N is the number of nodes in the linked list
    # Space Complexity: O(1)
    # We use a three pointer approach to reverse the linked list.  We keep track of the previous node, 
    # the current node, and the next node.
    # We iterate through the linked list and update the next pointer of the current node to point to the 
    # previous node. Then, we update the previous node to the current node, and the current node to the 
    # next node.
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

class OldSolution:
    # Time Complexity: O(N) where N is the number of nodes in the linked list
    # Space Complexity: O(N) 
    # We use a stack to store the nodes in the linked list.  We iterate through the linked list and push
    # each node onto the stack.  Then, we pop each node off the stack and append it to a new linked list.
    # We return the new linked list.
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        s = []
        sentinal = ListNode(0)
        currResult = sentinal
        while curr:
            s.append(curr)
            curr = curr.next
        while s:
            currResult.next = s.pop()
            currResult = currResult.next
        currResult.next = None
        return sentinal.next