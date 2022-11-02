# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        level = 0
        numOne = 0
        numTwo = 0
        while l1 or l2:
            if l1:
                numOne += (l1.val * pow(10, level))
                l1 = l1.next
            if l2:
                numTwo += (l2.val * pow(10, level))
                l2 = l2.next
            level += 1
        res = numOne + numTwo
        sentinal = ListNode(0)
        curr = sentinal
        if res == 0:
            return sentinal
        while res > 0:
            curr.next = ListNode(res % 10)
            curr = curr.next
            res = res//10
        return sentinal.next
