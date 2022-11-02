# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
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
