# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sentinal = ListNode(0)
        currResult = sentinal
        while list1 and list2:
            if list1.val < list2.val:
                currResult.next = list1
                list1 = list1.next
            else:
                currResult.next = list2
                list2 = list2.next
            currResult = currResult.next
        if list1:
                currResult.next = list1
        if list2:
                currResult.next = list2
        return sentinal.next
